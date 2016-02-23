from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from rapp.article.models import ArticleGroup

def index(request):
    template = get_template('index.html')
    context = {'article_groups': ArticleGroup.objects}
    return HttpResponse(template.render(context, request))
