# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-16 15:42
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0044_newspage_extro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='extro',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RawHTMLBlock())), blank=True),
        ),
    ]
