from django.http import HttpResponse
from django.template.loader import get_template
from rapp.article.models import Article
from django.views.generic.detail import DetailView

def index(request):
    template = get_template('index.html')
    context = {'articles': Article.objects.all()}
    return HttpResponse(template.render(context, request))

class ArticlesDetailView(DetailView):
    model = Article
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(Article, self).get_context_data(**kwargs)
        return context
