from django.db import models

# Create your models here.
class Procent(models.Model):
    city = models.TextField('Город',null= True)
    procent = models.FloatField('Доля от всех городов',default=0)
    class Meta:
        verbose_name="Таблица долей вакансий по городам"
        verbose_name_plural = "Доля вакансий по годам"
class Salary(models.Model):
    city = models.TextField('Город', null=True)
    salary = models.IntegerField('Доля от всех городов', default=0)
    class Meta:
        verbose_name="Таблица уровня зарплат по городам"
        verbose_name_plural = "Уровень зарплат по годам"


class GeographyGraphs(models.Model):
    pic = models.ImageField(upload_to='InfoVacancy/static/img', null=True, blank=True)
    class Meta:
        verbose_name="Графики вакансии за определённый год по городам"
        verbose_name_plural = "Графики"