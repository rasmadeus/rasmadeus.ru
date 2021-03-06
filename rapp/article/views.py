from django.http import HttpResponse
from django.template.loader import get_template
from rapp.article.models import Article
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


def _get_greeting(request):
    return request.user.username if request.user.is_authenticated() else "everyone"


def _get_default_common_data():
    return {
        'common_data': {
            'title': 'Developer blog',
            'keywords': 'c++, python, society life',
            'description': 'Developer blog',
            'author': 'K. Kulikov'
        }
    }


def index(request):
    template = get_template('index.html')
    context = {
        'greeting': _get_greeting(request),
        'article': _get_default_common_data()
    }
    return HttpResponse(template.render(context, request))


def code_404_view(request):
    template = get_template('404.html')
    context = {
        'greeting': _get_greeting(request),
        'article': _get_default_common_data()
    }
    return HttpResponse(template.render(context, request))


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['greeting'] = _get_greeting(self.request);
        return context


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['article'] = _get_default_common_data()
        context['greeting'] = _get_greeting(self.request);
        return context
