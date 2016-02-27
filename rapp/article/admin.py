from django.contrib import admin
from rapp.article import models
from django import forms
from redactor.widgets import RedactorEditor

admin.site.register(models.Article)

class EntryAdminForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ('content',)
        widgets = {
           'content': RedactorEditor(),
        }

class EntryAdmin(admin.ModelAdmin):
    form = EntryAdminForm
