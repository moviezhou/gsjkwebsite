# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-10 08:30
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0058_auto_20180620_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessdomain',
            name='dis_intro',
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name='二级页面显示简介'),
        ),
    ]
