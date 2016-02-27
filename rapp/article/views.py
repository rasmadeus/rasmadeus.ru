from django.http import HttpResponse
from django.template.loader import get_template
from rapp.article.models import Article
from django.views.generic.detail import DetailView
from django.contrib.auth import logout

def _get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def _get_greeting(request):
    greeting = request.user.username if request.user.is_authenticated() else "everyone"
    return greeting + " You are from: " + _get_client_ip(request)

def index(request):
    template = get_template('index.html')
    context = {'articles': Article.objects.all(), 'greeting': _get_greeting(request)}
    return HttpResponse(template.render(context, request))

def logout_view(request):
    logout(request)
    return index(request)

def code_404_view(request):
    template = get_template('404.html')
    context = {'greeting': _get_greeting(request)}
    return HttpResponse(template.render(context, request))


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['greeting'] = _get_greeting(self.request);
        return context
