from django.http import HttpResponse
from django.template.loader import get_template
from rapp.article.models import Article
from django.views.generic.detail import DetailView
from django.contrib.auth import logout


def _get_greeting(request):
    return request.user.username if request.user.is_authenticated() else "everyone"


def _get_default_common_data():
    return {
        'common_data': {
            'title': 'K. Kulikov home page',
            'keywords': 'c++, python, society life',
            'description': 'K. Kulikov blog',
            'author': 'K. Kulikov'
        }
    }

def index(request):
    template = get_template('index.html')
    context = {
        'articles': Article.objects.all(),
        'greeting': _get_greeting(request),
        'article': _get_default_common_data()
    }
    return HttpResponse(template.render(context, request))


def logout_view(request):
    logout(request)
    return index(request)


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
