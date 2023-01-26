from django.db import models

class Home(models.Model):
    text = models.TextField('Текст')
    have_picture = models.BooleanField('Изображение', null=True)
    pic = models.ImageField(upload_to='HomePage/static/HomePage/img', null=True, blank=True)
    right_pic= models.BooleanField('Картинка спарва в тексте?', null=True)
    have_header = models.BooleanField('Заголовок', null=True)
    class Meta:
        verbose_name="Главная"
        verbose_name_plural = "Главная"
