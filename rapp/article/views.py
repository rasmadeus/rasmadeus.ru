from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from rapp.article.models import ArticleGroup
from django.views.generic.detail import DetailView

def index(request):
    template = get_template('index.html')
    context = {'article_groups': ArticleGroup.objects.all()}
    return HttpResponse(template.render(context, request))

class ArticlesGroupDetailView(DetailView):
    model = ArticleGroup
    context_object_name = 'articles_group'

    def get_context_data(self, **kwargs):
        context = super(ArticleGroup, self).get_context_data(**kwargs)
        return context
