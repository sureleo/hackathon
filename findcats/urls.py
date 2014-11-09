from django.conf.urls import patterns, url

from findcats import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cat_id>\d+)/results/$', views.results, name='results'),
)
