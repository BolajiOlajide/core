# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-11 21:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealoption',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 8, 11, 21, 39, 31, 793000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mealoption',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 8, 11, 21, 39, 40, 929000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
