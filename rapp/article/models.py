from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from redactor.fields import RedactorField


class CommonData(models.Model):
    title = models.CharField(null=False, max_length=128, default='K. Kulikov home page', verbose_name='Page title')
    keywords = models.CharField(max_length=256, verbose_name='Keywords for search engines')
    description = models.CharField(max_length=256, verbose_name='Description of a web page')
    author = models.CharField(max_length=64, verbose_name='Author of a web page')

    def __unicode__(self):
        return self.title


def default_CommonData():
    default = CommonData.objects.get(title='K. Kulikov home page')
    if (default is None):
        default = CommonData()
        default.save()
    return default


class Article(models.Model):
    slug = models.SlugField(unique=True, null=False, default='article_slug', verbose_name='Url path')
    header = models.CharField(null=False, max_length=64, default='Article header', verbose_name='Header')
    description = models.TextField(null=False, default='Article description', verbose_name='Content')
    content = RedactorField(null=False, default='Article content', verbose_name='Content')
    author = models.ForeignKey(User, unique=False, null=False, verbose_name="Author")
    edit_time = models.DateTimeField(blank=False, verbose_name="Article edit time")
    prev_article = models.ForeignKey('Article', related_name='article_prev', unique=False, blank=True, null=True, verbose_name='Previous article')
    next_article = models.ForeignKey('Article', related_name='article_next', unique=False, blank=True, null=True, verbose_name='Next article')
    common_data = models.ForeignKey(CommonData, unique=False, blank=True, null=True, verbose_name='Meta data and header')

    def get_absolute_url(self):
        return "/{slug}/".format(slug=self.slug)

    def __unicode__(self):
        return self.header



