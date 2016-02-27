from django.http import HttpResponse
from django.template.loader import get_template
from rapp.article.models import Article
from django.views.generic.detail import DetailView
from django.contrib.auth import logout

def _build_header(request):
    if request.user.is_authenticated():
        return {'username': request.user.username, 'url': "/logout", 'caption': "Logout"}
    else:
        return {'username': "everyone", 'url': "/admin", 'caption': "Login"}


def index(request):
    template = get_template('index.html')
    context = {'articles': Article.objects.all(), 'header': _build_header(request)}
    return HttpResponse(template.render(context, request))


def logout_view(request):
    logout(request)
    return index(request)


def code_404_view(request):
    template = get_template('404.html')
    context = {'header': _build_header(request)}
    return HttpResponse(template.render(context, request))


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['header'] = _build_header(self.request);
        return context
