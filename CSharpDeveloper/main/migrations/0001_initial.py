# Generated by Django 4.1.4 on 2023-01-10 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='geography', max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(default=None, verbose_name='Заголовок')),
                ('table', models.TextField(default=None, verbose_name='Таблица')),
                ('graph', models.ImageField(default=None, upload_to='geographypage', verbose_name='График')),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='homepage', max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(default=None, verbose_name='Текст')),
                ('image', models.ImageField(default=None, upload_to='homepage', verbose_name='img')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='infopage', max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(default=None, verbose_name='Текст')),
                ('graph_left', models.ImageField(default=None, upload_to='infopage', verbose_name='График №2')),
                ('graph_right', models.ImageField(default=None, upload_to='infopage', verbose_name='График №1')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='skills', max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(default=None, verbose_name='Текст')),
            ],
        ),
    ]