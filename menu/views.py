from django.shortcuts import render
from .models import MenuItem, BusinessHours, ContactInfo

def home(request):
    items = MenuItem.objects.all()
    hours = BusinessHours.objects.first()
    contact = ContactInfo.objects.first()
    return render(request, 'menu/home.html', {
        'items': items,
        'hours': hours,
        'contact': contact,
    })