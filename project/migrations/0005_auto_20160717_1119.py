# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-17 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20160717_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='uid',
            field=models.IntegerField(),
        ),
    ]
