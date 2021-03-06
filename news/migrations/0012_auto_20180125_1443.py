# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-25 06:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20180125_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprisepage',
            name='enterprise_category',
            field=models.IntegerField(choices=[(1, '全资企业'), (2, '控股企业'), (3, '参股企业')], default=1, verbose_name='公司类型'),
        ),
        migrations.AlterField(
            model_name='enterprisepage',
            name='enterprise_intro',
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name='公司简介'),
        ),
        migrations.AlterField(
            model_name='enterprisepage',
            name='enterprise_logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='enterprisepage',
            name='enterprise_name',
            field=models.CharField(max_length=60, verbose_name='公司名称'),
        ),
        migrations.AlterField(
            model_name='enterprisepage',
            name='enterprise_website',
            field=models.CharField(blank=True, max_length=200, verbose_name='网址'),
        ),
    ]
