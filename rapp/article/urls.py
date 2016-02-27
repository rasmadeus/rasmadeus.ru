from django.conf.urls import url
import views

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', views.ArticleDetailView.as_view(), name='article'),
]