# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-03 17:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('wagtailcore', '0040_page_draft_title'),
        ('news', '0033_auto_20180306_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartybuildingTheories',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('theory_name', models.CharField(max_length=60, verbose_name='名称')),
                ('link_href', models.CharField(max_length=200, verbose_name='链接地址')),
                ('theory_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='背景图片')),
            ],
            options={
                'verbose_name': '理论苑地',
            },
            bases=('wagtailcore.page',),
        ),
    ]
