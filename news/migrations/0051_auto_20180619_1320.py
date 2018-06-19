# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-19 13:20
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0050_auto_20180619_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='stream_test',
            field=wagtail.core.fields.StreamField((('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_caption', wagtail.core.blocks.CharBlock(required=False))))),), blank=True),
        ),
    ]
