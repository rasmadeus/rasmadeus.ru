from django.conf.urls import include, url
from django.contrib import admin

from article.views import index

admin.autodiscover()

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
]
