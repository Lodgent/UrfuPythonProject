from django.db import models

class Skills(models.Model):
    year = models.IntegerField('Год',default=0)
    first_skill = models.TextField('1 скилл',default=0)
    second_skill = models.TextField('2 скилл',default=0)
    third_skill = models.TextField('3 скилл',default=0)
    forth_skill = models.TextField('4 скилл',default=0)
    fifth_skill = models.TextField('5 скилл',default=0)
    sixth_skill = models.TextField('6 скилл',default=0)
    seventh_skill = models.TextField('7 скилл',default=0)
    eighth_skill = models.TextField('8 скилл',default=0)
    ninth_skill = models.TextField('9 скилл',default=0)
    tenth_skill = models.TextField('10 скилл',default=0)
    class Meta:
        verbose_name="Топ скиллов за определённый год"
        verbose_name_plural = "Скиллы"
class SkillsGraphs(models.Model):
    pic = models.ImageField(upload_to='Skills/static/img', null=True, blank=True)
    class Meta:
        verbose_name="Графики скиллов за определённый год"
        verbose_name_plural = "Графики"