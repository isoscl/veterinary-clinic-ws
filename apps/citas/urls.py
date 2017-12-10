from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', report, name='report'),
    url(r'^create/(?P<clave>\w+)/(?P<fecha>[\d-]+)/(?P<rfc>\w+)/(?P<id>\w+)/(?P<hora>([0-1]\d|[2][0-3]):([0-5]\d))/(?P<diagnostico>.+)/(?P<total>\d+\.?\d+)/$', 
        create, name='create'),
    url(r'^(?P<clave>\w+)/$', read, name='read'),
    url(r'^(?P<clave>\w+)/update/(?P<fecha>[\d-]+)/(?P<rfc>\w+)/(?P<id>\w+)/(?P<hora>([0-1]\d|[2][0-3]):([0-5]\d))/(?P<diagnostico>.+)/(?P<total>\d+\.?\d+)/$', 
        update, name='update'),
    url(r'^(?P<clave>\w+)/delete/$', delete, name='delete'),
]
