# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 05:21
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timesdata', '0003_auto_20160421_0318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='station',
            name='lon',
        ),
        migrations.AddField(
            model_name='station',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, help_text='Represented as (longitude, latitude)', null=True, srid=4326),
        ),
    ]
