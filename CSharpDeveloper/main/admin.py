from django.contrib import admin
from .models import Home, Demand, Skills, Geography, TableDemand
from django.urls import reverse


# Register your models here.
admin.site.register(Home)
admin.site.register(Demand)
admin.site.register(TableDemand)
admin.site.register(Geography)
admin.site.register(Skills)




