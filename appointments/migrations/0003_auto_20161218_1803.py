# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-18 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_auto_20161213_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='duration',
            field=models.TimeField(default='00:30'),
        ),
    ]