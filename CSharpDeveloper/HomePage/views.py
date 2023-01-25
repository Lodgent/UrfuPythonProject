from django.shortcuts import render
from .models import Home

def HomePage(request):
    return render(request, 'HomePage/HomePage.html', {'data': Home.objects.all()})
