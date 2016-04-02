# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-02 20:05
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='article_slug', unique=True, verbose_name='Url path')),
                ('header', models.CharField(default='Article header', max_length=64, verbose_name='Header')),
                ('description', models.TextField(default='Article description', verbose_name='Content')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(default='Article content', verbose_name='Content')),
                ('edit_time', models.DateTimeField(verbose_name='Article edit time')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
        ),
        migrations.CreateModel(
            name='CommonData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='K. Kulikov home page', max_length=128, verbose_name='Page title')),
                ('keywords', models.CharField(max_length=256, verbose_name='Keywords for search engines')),
                ('description', models.CharField(max_length=256, verbose_name='Description of a web page')),
                ('author', models.CharField(max_length=64, verbose_name='Author of a web page')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='common_data',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article.CommonData', verbose_name='Meta data and header'),
        ),
        migrations.AddField(
            model_name='article',
            name='next_article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_next', to='article.Article', verbose_name='Next article'),
        ),
        migrations.AddField(
            model_name='article',
            name='prev_article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_prev', to='article.Article', verbose_name='Previous article'),
        ),
    ]