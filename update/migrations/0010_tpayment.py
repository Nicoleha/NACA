# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-02 14:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('update', '0009_auto_20190502_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tpayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('number_of_tickets', models.PositiveIntegerField(null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='update.Event')),
                ('ticket_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='update.Ticket')),
            ],
        ),
    ]