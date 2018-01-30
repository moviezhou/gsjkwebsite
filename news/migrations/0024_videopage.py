# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-30 05:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('news', '0023_auto_20180130_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('date', models.DateField(verbose_name='日期')),
                ('video_file_name', models.CharField(max_length=250, verbose_name='视频文件名称')),
                ('intro', models.CharField(max_length=250, verbose_name='简介')),
            ],
            options={
                'verbose_name': '视频内容',
            },
            bases=('wagtailcore.page',),
        ),
    ]
