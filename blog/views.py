# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.utils import timezone
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse


from blog.models import Article
from blog.forms import ArticleForm

def articles(request):
    latest_article_list = Article.objects.all().order_by('date_published')
   
    return render_to_response('blog/article_list.html',
    {'latest_article_list': latest_article_list,})

		
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
							  
							  
							  
def article_detail(request, article_id):
	article = Article.objects.filter(pk=article_id)
	#return HttpResponse('Details of Record: ' + article_id )
	return render_to_response('blog/article_detail.html',{'article_detail': article,})
