from django.shortcuts import render
from .vacancies import getvacancies
# Create your views here.

def vacancies(request):
    return render(request,'LastVacancies/LastVacancies.html',{'data':getvacancies()})
