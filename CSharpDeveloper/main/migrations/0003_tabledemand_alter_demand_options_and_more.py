# Generated by Django 4.1.5 on 2023-01-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_demand_delete_info_alter_geography_graph_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableDemand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('salary', models.IntegerField(verbose_name='Уровень зарплат')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('salary_by_prof', models.IntegerField(verbose_name='Уровень зарплат С#')),
                ('count_by_prof', models.IntegerField(verbose_name='Количество C#')),
            ],
            options={
                'verbose_name': 'Статистика вакансий за год',
                'verbose_name_plural': 'Вакансии',
            },
        ),
        migrations.AlterModelOptions(
            name='demand',
            options={'verbose_name': 'Информация о востребованности', 'verbose_name_plural': 'Информация о востребованности'},
        ),
        migrations.AlterModelOptions(
            name='geography',
            options={'verbose_name': 'География профессии', 'verbose_name_plural': 'География профессии'},
        ),
        migrations.AlterModelOptions(
            name='home',
            options={'verbose_name': 'Главная', 'verbose_name_plural': 'Главная'},
        ),
        migrations.AlterModelOptions(
            name='skills',
            options={'verbose_name': 'Информация о навыках', 'verbose_name_plural': 'Информация о навыках'},
        ),
    ]
