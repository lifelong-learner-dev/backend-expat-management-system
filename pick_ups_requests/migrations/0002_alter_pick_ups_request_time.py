# Generated by Django 4.1.7 on 2023-03-11 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pick_ups_requests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pick_ups_request',
            name='time',
            field=models.TimeField(default='19:00', verbose_name='Arrival or departure time'),
        ),
    ]
