from django.db import models

# Create your models here.
class Home(models.Model):
    text = models.TextField('Текст')
    have_picture = models.BooleanField('Изображение', null=True)
    pic = models.ImageField(upload_to='index/static/index/img', null=True, blank=True)
    have_header = models.BooleanField('Заголовок', null=True)
    class Meta:
        verbose_name="Главная"
        verbose_name_plural = "Главная"
