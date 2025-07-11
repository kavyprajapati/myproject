from django.shortcuts import render
from .models import *

# Create your views here.

def cars(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.POST.get('image')

        car.objects.create(
            name = name,
            price = price,
            image = image
        )
    return render(request, "carditails.html")