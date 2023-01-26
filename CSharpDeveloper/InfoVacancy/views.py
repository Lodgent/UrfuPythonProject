from django.shortcuts import render
from .models import Demand,DemandGraphs

def DemandInfo(request):
    return render(request, 'InfoVacancy/info.html', {'data': Demand.objects.all(),'graphs': DemandGraphs.objects.all()})
