from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import urls
import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rapp.article.views import index

admin.autodiscover()

urlpatterns = [
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^articles/', include("rapp.article.urls")),
    url(r'^$', index),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urls.handler404 = 'rapp.article.views.code_404_view'