from django.conf.urls import url
from rapp.article import views

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', views.ArticleDetailView.as_view(), name='articles_group'),
]