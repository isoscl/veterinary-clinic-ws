from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', report, name='report'),
    url(r'^create/(?P<clave>\w+)/(?P<descripcion>[\w\s]+)/(?P<precio>\d+\.?\d+)/$', create, name='create'),
    url(r'^(?P<clave>\w+)/$', read, name='read'),
    url(r'^(?P<clave>\w+)/update/(?P<descripcion>[\w\s]+)/(?P<precio>\d+\.?\d+)/$', update, name='update'),
    url(r'^(?P<clave>\w+)/delete/$', delete, name='delete'),
]
