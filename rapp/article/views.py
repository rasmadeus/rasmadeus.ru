from django.http import HttpResponse
from django.template.loader import get_template
from rapp.article.models import Article
from django.views.generic.detail import DetailView


class _Header:
    def __init__(self, request):
        if request.user.is_authenticated():
            self._username = request.user.username
            self._url = "/logout"
            self._caption = "Logout"
        else:
            self._username = "everyone"
            self._url = "/admin"
            self._caption = "Login"

    def username(self):
        return self._username

    def url(self):
        return self._url

    def caption(self):
        return self._caption


def index(request):
    template = get_template('index.html')
    context = {'articles': Article.objects.all(), 'header': _Header(request)}
    return HttpResponse(template.render(context, request))


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['username'] = _Header(self.request);
        return context
