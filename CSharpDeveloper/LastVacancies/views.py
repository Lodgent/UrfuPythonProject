from django.shortcuts import render
from .vacancies import get_vacancies
def vacancies(request):
    return render(request,'LastVacancies/vacancy.html',{'data':get_vacancies()})
