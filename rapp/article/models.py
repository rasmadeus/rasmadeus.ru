from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Article(models.Model):
    slug = models.CharField(unique=True, null=False, max_length=64, verbose_name="Url path")
    header = models.CharField(null=False, max_length=64, verbose_name="Header")
    content = models.TextField(null=False, verbose_name="Content")
    author = models.ForeignKey(User, verbose_name="Author")
    edit_time = models.DateTimeField(default=datetime.now(), blank=True, verbose_name="Article edit time")

    def get_absolute_url(self):
        return "/{slug}/".format(slug=self.slug)

    def __unicode__(self):
        return self.header


class ArticleGroup(models.Model):
    slug = models.CharField(unique=True, null=False, max_length=64, verbose_name="Url path")
    header = models.CharField(null=False, max_length=64, verbose_name="Header")
    description = models.TextField(null=False, verbose_name="Description")
    articles = models.ManyToManyField(Article, verbose_name="Articles")

    def get_absolute_url(self):
        return "/{slug}/".format(slug=self.slug)

    def __unicode__(self):
        return self.header


