# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0003_result_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=0, default=None, max_digits=10, null=True),
        ),
    ]
