# Generated by Django 4.1.7 on 2023-03-05 19:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='passport_expiry_date',
            field=models.DateField(default=datetime.date.today, verbose_name='passport expiry date'),
        ),
    ]
