from django.shortcuts import render
from .models import  SkillsGraphs, Skills

def Skills_func(request):
    return render(request, 'Skills/skills.html', {'data': Skills.objects.all(),'graphs': SkillsGraphs.objects.all()})