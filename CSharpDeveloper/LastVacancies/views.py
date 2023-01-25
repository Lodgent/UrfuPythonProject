from django.shortcuts import render
from .vacancies import get_vacancies
# Create your views here.

def vacancies(request):
    return render(request,'LastVacancies/vacancy.html',{'data':get_vacancies()})
