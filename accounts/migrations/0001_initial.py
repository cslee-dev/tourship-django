# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 15:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50, verbose_name='상세주소')),
                ('birthdate', models.CharField(blank=True, max_length=120, verbose_name='생일')),
                ('gender', models.CharField(max_length=5, verbose_name='성별')),
                ('phone_num', models.CharField(max_length=15, verbose_name='전화번호')),
                ('photo', models.ImageField(blank=True, upload_to='newspeed/%Y/%m/%d/', verbose_name='프로필사진')),
                ('is_tour', models.BooleanField(default=False, verbose_name='여행여부')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
