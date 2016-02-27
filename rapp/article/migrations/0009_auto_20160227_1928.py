# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 19:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20160227_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='next_article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_next', to='article.Article', verbose_name='Next article'),
        ),
        migrations.AddField(
            model_name='article',
            name='prev_article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_prev', to='article.Article', verbose_name='Previous article'),
        ),
    ]