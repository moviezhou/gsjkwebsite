# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-25 06:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20180125_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprisepage',
            name='enterprise_category',
            field=models.IntegerField(choices=[('全资企业', '全资企业'), ('控股企业', '控股企业'), ('参股企业', '参股企业')], default=1, verbose_name='公司类型'),
        ),
        migrations.AlterField(
            model_name='newspage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='newspage',
            name='date',
            field=models.DateField(verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='newspage',
            name='intro',
            field=models.CharField(max_length=250, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='newspage',
            name='representative_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='缩略图'),
        ),
    ]
