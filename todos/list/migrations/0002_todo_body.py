# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-12 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='body',
            field=models.TextField(default=''),
        ),
    ]
