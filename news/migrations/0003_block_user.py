# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 20:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_auto_20170816_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_man', models.CharField(max_length=20, verbose_name='차단된 유저명')),
                ('reasons', models.CharField(max_length=20, verbose_name='차단사유')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
