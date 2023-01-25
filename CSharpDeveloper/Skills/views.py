from django.shortcuts import render
from .models import  SkillsGraphs, Skills
# Create your views here.

def Skills_func(request):
    data = Skills.objects.all()
    dataGraphs = SkillsGraphs.objects.all()
    return render(request, 'Skills/skills.html', {'data': data,'graphs': dataGraphs})