import datetime

from django.db import models
from django.urls import reverse

# Create your models here


class Home(models.Model):
    title = models.CharField('Заголовок', max_length=100, default='homepage')
    text = models.TextField('Текст', default=None)
    image = models.ImageField(
        'img', default=None,
        upload_to='home'
    )
    class Meta:
        verbose_name="Главная"
        verbose_name_plural = "Главная"


class Demand(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='demand'
    )
    text = models.TextField('Текст', default=None)
    graph_left = models.ImageField(
        'График №2',
        default=None,
        upload_to='demand'
    )
    graph_right = models.ImageField(
        'График №1',
        default=None,
        upload_to='demand'
    )
    class Meta:
        verbose_name="Информация о востребованности"
        verbose_name_plural ="Информация о востребованности"


class Geography(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='geography'
    )
    text = models.TextField('Заголовок', default=None)
    table = models.TextField('Таблица', default=None)
    graph = models.ImageField(
        'График',
        default=None,
        upload_to='geography'
    )
    class Meta:
        verbose_name="География профессии"
        verbose_name_plural ="География профессии"

class Skills(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='skills'
    )
    text = models.TextField('Текст', default=None)
    class Meta:
        verbose_name="Информация о навыках"
        verbose_name_plural ="Информация о навыках"
