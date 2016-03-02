from django.contrib import admin
from rapp.article import models
from django import forms
from redactor.widgets import RedactorEditor

admin.site.register(models.Article)
admin.site.register(models.CommonData)
