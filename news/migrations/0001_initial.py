# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 16:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='주소')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='댓글내용')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(blank=True, upload_to='sub_photo/%Y/%m/%d/', verbose_name='사진')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('tourday', models.DateField(verbose_name='여행날짜')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('main_photo', models.ImageField(blank=True, upload_to='main_photo/%Y/%m/%d/', verbose_name='사진')),
            ],
        ),
        migrations.CreateModel(
            name='Postprivacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy', models.CharField(max_length=15, verbose_name='정책')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='privacy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_posts', to='news.Postprivacy', verbose_name='Privacy related'),
        ),
        migrations.AddField(
            model_name='photo',
            name='pos',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='news.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_comments', to='news.Post', verbose_name='post related'),
        ),
        migrations.AddField(
            model_name='address',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_addresss', to='news.Post', verbose_name='post related'),
        ),
    ]
