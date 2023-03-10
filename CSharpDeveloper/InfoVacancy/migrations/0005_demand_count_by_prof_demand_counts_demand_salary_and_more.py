# Generated by Django 4.1.5 on 2023-01-24 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfoVacancy', '0004_alter_demand_options_remove_demand_have_header_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='demand',
            name='count_by_prof',
            field=models.IntegerField(default=0, verbose_name='Количество вакансий C#'),
        ),
        migrations.AddField(
            model_name='demand',
            name='counts',
            field=models.IntegerField(default=0, verbose_name='Количество'),
        ),
        migrations.AddField(
            model_name='demand',
            name='salary',
            field=models.IntegerField(default=0, verbose_name='Уровень зарплат'),
        ),
        migrations.AddField(
            model_name='demand',
            name='salary_by_prof',
            field=models.IntegerField(default=0, verbose_name='Уровень зарплат C#'),
        ),
        migrations.AddField(
            model_name='demand',
            name='year',
            field=models.IntegerField(default=0, verbose_name='Год'),
        ),
    ]
