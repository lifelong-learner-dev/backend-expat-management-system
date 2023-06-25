# Generated by Django 4.1.7 on 2023-06-25 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Green_card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=180)),
                ('green_card_expiry_date', models.DateField(blank=True, null=True)),
                ('overseas_car_insurance_expiry_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Green cards',
            },
        ),
    ]
