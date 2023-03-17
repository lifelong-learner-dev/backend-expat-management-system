# Generated by Django 4.1.7 on 2023-03-17 20:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=180)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('detailed_information', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name_plural': 'Documents',
            },
        ),
        migrations.CreateModel(
            name='Explanation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=180)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('detailed_information', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name_plural': 'Explanations',
            },
        ),
        migrations.CreateModel(
            name='Visit_place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=180)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('detailed_information', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name_plural': 'Visit places',
            },
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=180)),
                ('subject', models.CharField(blank=True, choices=[('work_permits', 'Work permits'), ('real_estate_agents', 'Real estate agents'), ('pick_ups', 'Pick ups'), ('moving_companies', 'Moving companies'), ('moving', 'Moving'), ('houses', 'Houses'), ('green_cards', 'Green cards'), ('family_residence_permtis', 'Family residence permits'), ('driving_licenses', 'Driving licenses'), ('company_cars', 'Company cars')], max_length=30)),
                ('start_date', models.DateField(default=datetime.date.today, verbose_name='Start date?')),
                ('start_time', models.TimeField(default='19:00', verbose_name='Start time')),
                ('finish_date', models.DateField(default=datetime.date.today, verbose_name='Finish date')),
                ('finish_time', models.TimeField(default='19:00', verbose_name='Finish time')),
                ('documents', models.ManyToManyField(related_name='announcements', to='announcements.document')),
                ('explanations', models.ManyToManyField(related_name='announcements', to='announcements.explanation')),
                ('visit_place', models.ManyToManyField(related_name='announcements', to='announcements.visit_place')),
            ],
            options={
                'verbose_name_plural': 'Announcements',
            },
        ),
    ]