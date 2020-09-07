""""Pet views."""

# Django
from django.shortcuts import render, redirect

# Forms
from .forms import PetForm

# Models
from .models import Pet, MedicalServices
from django.contrib.auth.models import User

# Create your views here.

def CreatePet(request):
    if request.method == 'GET':
        form = PetForm()
        return render(request, 'pet/create_pet.html', {'form': form})

    elif request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            Pet.objects.create(user=request.user,
                               name=form['name'].data, 
                               pet_type=form['pet_type'].data,
                               size=form['size'].data,
                               description=form['description'].data
                               )
            return redirect('create_pet')        
        return render(request, 'pet/create_pet.html', {'form': form})
    
def historyPet(request):
    pet = Pet.objects.filter(user_id=request.user.id)
    histories = []
    history = MedicalServices.objects.filter(pet_id=request.user.id).values('service_type', 'date')
    for h in history:
        service = ''
        if h['service_type'] == '1':
            service = 'Consulta'
        elif h['service_type'] == '2':
            service = 'Cita de vacunación'
        elif h['service_type'] == '3':            
            service = 'Cita de desparacitación'
        elif h['service_type'] == '4':
            service = 'Cita de baño'
        elif h['service_type'] == '5':
            service = 'Cita de corte de pelo'
        date = h['date'].strftime('%A %d de %B')
        hour = h['date'].strftime('%H:%M %p')
        histories.append({'service': h['service_type'], 'service_type': service, 'date': date, 'hour': hour, 'datetime': h['date']})

    return render(request, 'pet/history.html', {'pet': pet[0], 'histories': histories})
