# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 09:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='station',
            new_name='station_name',
        ),
    ]