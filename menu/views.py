from django.shortcuts import render
from .models import MenuItem

# Create your views here.

def home(request):
    items = MenuItem.objects.all()
    return render(request, 'menu/home.html', {'items': items})