from __future__ import unicode_literals

from django.db import models

class ArticleGroup(models.Model):
    slug = models.CharField(unique=True, null=False, max_length=64, verbose_name="Url path")
    header = models.CharField(null=False, max_length=64, verbose_name="Header")
    description = models.TextField(null=False, verbose_name="Description")

    def get_absolute_url(self):
        return "/{slug}/".format(slug=self.slug)

    def __unicode__(self):
        return self.header
