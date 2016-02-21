from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^$', include('rapp.article.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
