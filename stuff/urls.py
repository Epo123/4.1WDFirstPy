from django.conf.urls import patterns, url

from stuff import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(\w+/$)', views.index, name='index'))
