# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-30 22:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginreg', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='title',
        ),
    ]
