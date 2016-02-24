from django.conf.urls import url
import views

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', views.ArticlesDetailView.as_view(), name='articles'),
]