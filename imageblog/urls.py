from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# User imports
from blog.views import articles, article_add, article_detail

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'imageblog.views.home', name='home'),
    # url(r'^imageblog/', include('imageblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^add_article/$', article_add),
	url(r'^article_detail/(?P<article_id>\d)$', article_detail),
    url(r'^$', articles, name='article-list'),
)
