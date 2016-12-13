# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-12-11 23:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(blank=True, max_length=50, null=True, verbose_name='Subject')),
                ('Content', models.TextField(blank=True, null=True, verbose_name='Content')),
                ('Recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Recipient')),
                ('Sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sender', to=settings.AUTH_USER_MODEL, verbose_name='Sender')),
            ],
        ),
    ]
