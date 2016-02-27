from django.conf.urls import include, url
from django.contrib import admin
from rapp.article.views import index, logout_view
from django.conf import urls
from django_markdown import flatpages

admin.autodiscover()
flatpages.register()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^logout/', logout_view),
    url(r'^articles/', include("rapp.article.urls")),
    url(r'^$', index),
]

urls.handler404 = 'rapp.article.views.code_404_view'