# Generated by Django 4.1.5 on 2023-01-24 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InfoVacancy', '0003_rename_home_demand'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='demand',
            options={'verbose_name': 'Таблица', 'verbose_name_plural': 'Таблица'},
        ),
        migrations.RemoveField(
            model_name='demand',
            name='have_header',
        ),
        migrations.RemoveField(
            model_name='demand',
            name='have_picture',
        ),
        migrations.RemoveField(
            model_name='demand',
            name='pic',
        ),
        migrations.RemoveField(
            model_name='demand',
            name='right_pic',
        ),
        migrations.RemoveField(
            model_name='demand',
            name='text',
        ),
    ]
