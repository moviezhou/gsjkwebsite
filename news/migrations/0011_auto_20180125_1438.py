# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-25 06:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('wagtailcore', '0040_page_draft_title'),
        ('news', '0010_columnpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnterprisePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('enterprise_category', models.IntegerField(choices=[(1, '全资企业'), (2, '控股企业'), (3, '参股企业')], default=1)),
                ('enterprise_name', models.CharField(max_length=60)),
                ('enterprise_intro', wagtail.core.fields.RichTextField(blank=True)),
                ('enterprise_website', models.CharField(blank=True, max_length=200)),
                ('enterprise_logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': '企业',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterModelOptions(
            name='newspage',
            options={'verbose_name': '新闻'},
        ),
    ]
