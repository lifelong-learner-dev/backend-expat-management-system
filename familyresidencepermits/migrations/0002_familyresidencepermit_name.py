# Generated by Django 4.1.7 on 2023-03-06 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familyresidencepermits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='familyresidencepermit',
            name='name',
            field=models.CharField(default='', max_length=180),
        ),
    ]
