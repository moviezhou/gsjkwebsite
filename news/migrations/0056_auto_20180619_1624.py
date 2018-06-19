# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-19 16:24
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0055_auto_20180619_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='image_streamfield',
            field=wagtail.core.fields.StreamField((('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(classname='news-image', label='图片', required=True)), ('image_caption', wagtail.core.blocks.CharBlock(label='图片摘要', required=False))))),), verbose_name='插入图片'),
        ),
    ]
