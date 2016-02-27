from django.conf.urls import include, url
from django.contrib import admin
from rapp.article.views import index, logout_view
from django.conf.urls import  handler404

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/', logout_view),
    url(r'^articles/', include("rapp.article.urls")),
    url(r'^$', index),
]

handler404 = 'rapp.article.views.code_404_view'