from django.conf.urls import include, url
from django.contrib import admin
from rapp.article.views import index, logout_view

admin.autodiscover()

urlpatterns = [
    url(r'^login/', include(admin.site.urls)),
    url(r'^logout/', logout_view),
    url(r'^articles/', include("rapp.article.urls")),
    url(r'^$', index),
]
