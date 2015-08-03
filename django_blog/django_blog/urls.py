from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import index
from django.conf import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.home', name='home'),

    url('^blog/archive/(?P<year>[\d]+)/(?P<month>[\d]+)/$', 'blog.views.date_archive', name="blog_date_archive"),
    url('^blog/archive/(?P<slug>[-\w]+)/$', 'blog.views.category_archive', name="blog_category_archive"),
    url('^blog/(?P<slug>[-\w]+)/$', 'blog.views.single', name="blog_article_single"),
    url('^blog/(?P<slug>[-\w]+)/likes/$', 'blog.views.likes', name="blog_article_single_likes"), 
    url('^blog/$', 'blog.views.index', name="blog_article_index"),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^search/', include('haystack.urls')),
    url('^about/$', 'blog.views.about', name="blog_about"), 
    
)


if settings.DEBUG is False:
    urlpatterns += patterns('', url(r'^static1/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,}),)
