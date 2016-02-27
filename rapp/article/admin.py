from django.contrib import admin
from rapp.article import models
from django_markdown.admin import MarkdownModelAdmin

admin.site.register(models.Article, MarkdownModelAdmin)