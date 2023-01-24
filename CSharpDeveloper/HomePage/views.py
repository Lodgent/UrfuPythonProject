from django.shortcuts import render
from .models import Home
# Create your views here.

def HomePage(request):
    data = Home.objects.all()
    return render(request, 'HomePage/HomePage.html', {'data': data})
