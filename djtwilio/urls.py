from django.conf.urls import patterns, url

from djtwilio import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^sms/$', views.sms, name='sms'),
)
