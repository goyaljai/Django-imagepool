# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-17 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField(max_length=1000)),
                ('caption', models.TextField(max_length=1000)),
                ('like_count', models.IntegerField(default=0, max_length=1000)),
                ('access_users', models.TextField(default='public', max_length=1000)),
                ('uid', models.IntegerField(max_length=1000)),
            ],
        ),
    ]
