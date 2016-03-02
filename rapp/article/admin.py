from django.contrib import admin
from rapp.article import models
from django import forms


admin.site.register(models.Article)
admin.site.register(models.CommonData)
