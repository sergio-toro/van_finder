# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='province',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]