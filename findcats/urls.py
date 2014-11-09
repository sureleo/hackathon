from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from findcats import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cat_id>\d+)/results/$', views.results, name='results')
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
