# Generated by Django 4.1.5 on 2023-01-24 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfoVacancy', '0006_alter_demand_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemandGraphs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(blank=True, null=True, upload_to='InfoVacancy/static/img')),
            ],
            options={
                'verbose_name': 'Графики вакансии за определённый год',
                'verbose_name_plural': 'Графики',
            },
        ),
    ]
