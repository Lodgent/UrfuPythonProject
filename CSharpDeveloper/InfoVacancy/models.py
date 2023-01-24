from django.db import models

# Create your models here.
class Demand(models.Model):
    year = models.IntegerField('Год',default=0)
    salary = models.IntegerField('Уровень зарплат',default=0)
    counts = models.IntegerField('Количество',default=0)
    salaryJob = models.IntegerField('Уровень зарплат C#',default=0)
    countJob = models.IntegerField('Количество вакансий C#',default=0)
    class Meta:
        verbose_name="Информацию о вакансии за определённый год"
        verbose_name_plural = "Вакансии"
class DemandGraphs(models.Model):
    pic = models.ImageField(upload_to='InfoVacancy/static/img', null=True, blank=True)
    class Meta:
        verbose_name="Графики вакансии за определённый год"
        verbose_name_plural = "Графики"