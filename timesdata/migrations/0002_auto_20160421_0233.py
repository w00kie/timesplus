# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 02:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesdata', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='id',
        ),
        migrations.AlterField(
            model_name='station',
            name='code',
            field=models.CharField(max_length=6, primary_key=True, serialize=False),
        ),
    ]