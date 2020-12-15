from django.shortcuts import render

# Untuk percobaan pakai HttpResponse
from django.http import HttpResponse

def home(request):
    return HttpResponse('<p>home view</p>')

def pet_detail(request, pet_id):
    return HttpResponse(f'<p>pet_detail view with id {pet_id} </p>')