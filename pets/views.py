""""Pet views."""

# Django
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

# Forms
from .forms import PetForm, MedicalServicesForm

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

def meet(request):
    pet = Pet.objects.filter(user_id=request.user.id)
    histories = []
    history = MedicalServices.objects.filter(pet_id=request.user.id).values('id', 'service_type', 'date')
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
        histories.append({'id': h['id'], 'service': h['service_type'], 'service_type': service, 'date': date, 'hour': hour, 'datetime': h['date']})

    return render(request, 'pet/meet.html', {'pet': pet[0], 'histories': histories})

def new_meet(request):
    if request.method == 'GET':
        form = MedicalServicesForm()
        return render(request, 'pet/new_meet.html', {'form': form})
    if request.method == 'POST':
        form = MedicalServicesForm(request.POST)
        if form.is_valid():
            pet = Pet.objects.get(user_id=request.user.id)
            print(pet)
            print(pet, form['service_type'].data, form['date'].data,)
            MedicalServices.objects.create(pet=pet,
                               service_type=form['service_type'].data, 
                               date=form['date'].data,
                               )
            return redirect('meet')
        return redirect('meet')

def edit_meet(request, id_meet):

    try:
        meet = MedicalServices.objects.get(id=id_meet)
        form = MedicalServicesForm(request.POST or None, instance=meet)
        #import pdb; pdb.set_trace()
        if form.is_valid():
            form.save()
            return redirect('meet')

        context = {
            'form': form,
            'id_meet': id_meet,
        }

        return render(request, 'pet/edit_meet.html', context)

    except:
        context = {
            'form': None,
            'id_meet': id_meet,
        }

        return render(request, 'pet/edit_meet.html', context)

def delete_meet(request, id_meet):

    meet = MedicalServices.objects.get(id=id_meet)
    if request.method == 'POST':
        meet.delete()
        return redirect('meet')

    context = {
        'meet': meet,
        'id_meet': id_meet
    }

    return render(request, 'pet/delete_meet.html', context)