""""Pet views."""

# Django
from django.shortcuts import render, redirect

# Forms
from .forms import PetForm

# Models
from .models import Pet
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
    pass
