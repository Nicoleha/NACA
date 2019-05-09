# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-02 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('update', '0008_auto_20190502_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date_of_event',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(null=True, verbose_name='Starting time for the event'),
        ),
    ]
