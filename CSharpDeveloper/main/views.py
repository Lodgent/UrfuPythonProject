from django.shortcuts import render
from .models import Home, Demand, Skills, Geography, TableDemand
from .utils import get_vacancies


def home(request):
    homepage = Home.objects.all()[0]
    return render(
        request,
        'main/home.html',
        context={
            'homepage': homepage,
        }
    )


def info(request):

    infopage = Demand.objects.all()[0]
    demandtable = TableDemand.objects.all()
    return render(
        request,
        'main/info.html',
        context={
            'infopage': infopage,
            'tabledemand': demandtable,
        }
    )


def geography(request):
    geographypage = Geography.objects.all()[0]
    return render(
        request,
        'main/geography.html',
        context={
            'geographypage': geographypage,
        }
    )


def vacancies(request):
    return render(request, 'main/vacanvies_template.html',
                  context={'vacancies': get_vacancies(), })


def skills(request):
    skillspage = Skills.objects.all()[0]
    return render(
        request,
        'main/skills.html',
        context={
            'skillspage': skillspage,
        }
    )

