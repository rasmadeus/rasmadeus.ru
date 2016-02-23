from django.contrib import admin
from rapp.article import models

admin.site.register(models.ArticleGroup)
admin.site.register(models.Article)