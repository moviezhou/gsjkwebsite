# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-09 02:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0042_newspage_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newspage',
            name='table',
        ),
    ]