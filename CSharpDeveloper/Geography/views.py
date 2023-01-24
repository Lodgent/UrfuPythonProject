from django.shortcuts import render
from .models import Salary,Procent,GeographyGraphs
# Create your views here.

def Geography(request):
    data_salary = Salary.objects.all()
    data_procent= Procent.objects.all()
    data_graphs = GeographyGraphs.objects.all()
    return render(request, 'Geography/Geography.html', {'data_salary': data_salary,'data_procent': data_procent,'data_graphs': data_graphs})

# Create your views here.
