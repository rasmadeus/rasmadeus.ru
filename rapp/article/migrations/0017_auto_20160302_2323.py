# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 23:23
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0016_auto_20160302_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(default='Article content', verbose_name='Content'),
        ),
    ]