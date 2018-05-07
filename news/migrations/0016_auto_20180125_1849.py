# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-25 18:49
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_businessdomain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessdomain',
            name='business_intro',
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name='领域简介'),
        ),
    ]
