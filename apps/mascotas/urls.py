from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', report, name='report'),
    url(r'^create/(?P<id>\w+)/(?P<rfc>\w+)/(?P<nombre>[\w\s]+)/(?P<especie>[\w\s]+)/(?P<raza>[\w\s]+)/(?P<color>[\w\s]+)/(?P<tamanio>[\w\s]+)/(?P<senia>[\w\s]+)/(?P<fecha>[\d-]+)/$', 
        create, name='create'),
    url(r'^(?P<id>\w+)/$', read, name='read'),
    url(r'^(?P<id>\w+)/update/(?P<rfc>\w+)/(?P<nombre>[\w\s]+)/(?P<especie>[\w\s]+)/(?P<raza>[\w\s]+)/(?P<color>[\w\s]+)/(?P<tamanio>[\w\s]+)/(?P<senia>[\w\s]+)/(?P<fecha>[\d-]+)/$', 
        update, name='update'),
    url(r'^(?P<id>\w+)/delete/$', delete, name='delete'),
]
