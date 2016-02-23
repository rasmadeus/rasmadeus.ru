from django.conf.urls import include, url
from django.contrib import admin
from rapp.article.views import index

admin.autodiscover()

urlpatterns = [
    url(r'$', index, name='index'),
    url(r'^articles_group/', include("rapp.article.urls")),
    url(r'^admin/', include(admin.site.urls)),
]
