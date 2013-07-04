from django.conf.urls import patterns, include, url

urlpatterns = patterns('manual.views',
    url(r'^$', 'index', name='manual_index'),
    url(r'^(?P<slug>[-\w]+)/$', 'view_page', name='manual_view_page'),
)
