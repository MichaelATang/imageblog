# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.utils import timezone
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse


from blog.models import Article
from blog.forms import ArticleForm

class Index(ListView):

    model = Article

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

		
def article_add(request):
    # sticks in a POST or renders empty form
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        cmodel = form.save()
        #This is where you might chooose to do stuff.
        #cmodel.name = 'test1'
        cmodel.save()
        return HttpResponse('Record Saved!')

    return render_to_response('blog/contact.html',
                              {'article_form': form},
                              context_instance=RequestContext(request))