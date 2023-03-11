# Generated by Django 4.1.7 on 2023-03-11 18:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('work_permits', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Work_permits_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=180)),
                ('location', models.CharField(default='', max_length=180)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='When did you lose the card?')),
                ('krstatus', models.CharField(blank=True, choices=[('informed', '워크퍼밋 카드를 잃어버렸어요'), ('checked', '총무팀 확인'), ('reapplied', '재신청 완료'), ('waitingforapproval', '승인 대기 중'), ('approvedandwaitforcard', '승인됨 카드 발급 대기 중'), ('completed', '카드 발급 및 전달 완료, 모든 절차 완료')], max_length=150)),
                ('enstatus', models.CharField(blank=True, choices=[('informed', 'I have lost my card'), ('checked', 'GA team member checked the request'), ('reapplied', 'Re-applied'), ('waitingforapproval', 'Waiting for approval'), ('approvedandwaitforcard', 'Approved and waiting for card'), ('completed', 'Card issued and delivered, Completed')], max_length=150)),
                ('expat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_permits_requests', to=settings.AUTH_USER_MODEL)),
                ('work_permit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_permits_requests', to='work_permits.work_permit')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
