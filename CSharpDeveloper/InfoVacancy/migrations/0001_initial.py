# Generated by Django 4.1.5 on 2023-01-24 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('salary', models.IntegerField(verbose_name='Уровень зарплат')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('salary_job', models.IntegerField(verbose_name='Уровень зарплат С#')),
                ('count_job', models.IntegerField(verbose_name='Количество C#')),
            ],
            options={
                'verbose_name': 'Статистика вакансий за определённый год',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]
