# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-19 02:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('wagtailcore', '0040_page_draft_title'),
        ('news', '0043_remove_newspage_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubAdBanner',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('link_href', models.CharField(blank=True, max_length=200, verbose_name='链接地址')),
                ('banner_img', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='广告图片')),
            ],
            options={
                'verbose_name': '广告banner',
            },
            bases=('wagtailcore.page',),
        ),
    ]
