from django.conf.urls import url
from rapp.article.views import ArticleListView
import views

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='article-list'),
    url(r'^(?P<slug>[-\w]+)/$', views.ArticleDetailView.as_view(), name='article'),
]