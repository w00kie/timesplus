# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 03:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesdata', '0002_auto_20160421_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='closing',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='station',
            name='new',
            field=models.BooleanField(default=False),
        ),
    ]
