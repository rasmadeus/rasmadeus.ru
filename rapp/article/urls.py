from django.conf.urls import url
import views

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', views.ArticlesGroupDetailView.as_view(), name='articles_group'),
]