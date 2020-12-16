from django.shortcuts import render

from django.http import Http404
from .models import Pet # import Pet model from models.py

def home(request):
    pets = Pet.objects.all() # <- query ORM 
    return render(request, 'home.html', {
        'pets': pets, # <- render function takes a dictionary with the data we want to make available inside of template
    })

def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')

    return render(request, 'pet_detail.html', {
        'pet': pet,
    })
