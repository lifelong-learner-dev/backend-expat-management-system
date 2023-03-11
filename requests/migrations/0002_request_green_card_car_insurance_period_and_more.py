# Generated by Django 4.1.7 on 2023-03-07 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('green_cards', '0001_initial'),
        ('moving', '0001_initial'),
        ('pick_ups', '0001_initial'),
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='Green_card_car_insurance_period',
            field=models.CharField(blank=True, choices=[('one_month', 'One month'), ('three_months', 'Three months'), ('six_months', 'Six months'), ('a_year', 'A year')], max_length=50),
        ),
        migrations.AddField(
            model_name='request',
            name='green_card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requests', to='green_cards.green_card'),
        ),
        migrations.AddField(
            model_name='request',
            name='green_card_departure_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='moving',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requests', to='moving.moving'),
        ),
        migrations.AddField(
            model_name='request',
            name='name',
            field=models.CharField(default='', max_length=180),
        ),
        migrations.AddField(
            model_name='request',
            name='pick_up',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requests', to='pick_ups.pick_up'),
        ),
        migrations.AddField(
            model_name='request',
            name='request_subject',
            field=models.CharField(blank=True, choices=[('green_card', 'Green card'), ('moving', 'Moving'), ('pick_up', 'Pick up')], max_length=50),
        ),
        migrations.AddField(
            model_name='request',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL),
        ),
    ]