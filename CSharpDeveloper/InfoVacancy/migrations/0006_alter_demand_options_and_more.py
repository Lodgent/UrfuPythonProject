# Generated by Django 4.1.5 on 2023-01-24 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InfoVacancy', '0005_demand_count_by_prof_demand_counts_demand_salary_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='demand',
            options={'verbose_name': 'Информацию о вакансии за определённый год', 'verbose_name_plural': 'Вакансии'},
        ),
        migrations.RenameField(
            model_name='demand',
            old_name='count_by_prof',
            new_name='countJob',
        ),
        migrations.RenameField(
            model_name='demand',
            old_name='salary_by_prof',
            new_name='salaryJob',
        ),
    ]
