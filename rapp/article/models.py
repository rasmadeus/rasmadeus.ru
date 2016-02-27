from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    slug = models.SlugField(unique=True, null=False, verbose_name="Url path")
    header = models.CharField(null=False, max_length=64, verbose_name="Header")
    content = models.TextField(null=False, verbose_name="Content")
    author = models.ForeignKey(User, unique=False, null=False, verbose_name="Author")
    edit_time = models.DateTimeField(blank=False, verbose_name="Article edit time")
    prev_article = models.ForeignKey('Article', related_name="article_prev", unique=False, blank=True, null=True, verbose_name="Previous article")
    next_article = models.ForeignKey('Article', related_name="article_next", unique=False, blank=True, null=True, verbose_name="Next article")

    def get_absolute_url(self):
        return "/{slug}/".format(slug=self.slug)

    def __unicode__(self):
        return self.header



