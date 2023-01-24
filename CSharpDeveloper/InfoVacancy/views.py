from django.shortcuts import render
from .models import Demand,DemandGraphs
# Create your views here.

def DemandInfo(request):
    data = Demand.objects.all()
    dataGraphs = DemandGraphs.objects.all()
    return render(request, 'InfoVacancy/info.html', {'data': data,'graphs': dataGraphs})
