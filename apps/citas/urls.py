from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', report, name='report'),
    url(r'^create/(?P<fecha>.+)/(?P<rfc>.+)/(?P<id>.+)/(?P<hora>.+)/(?P<diagnostico>.+)/(?P<total>.+)/$', 
        create, name='create'),
    url(r'^(?P<clave>.+)/delete/$', delete, name='delete'),
    url(r'^(?P<clave>.+)/update/(?P<fecha>.+)/(?P<rfc>.+)/(?P<id>.+)/(?P<hora>.+)/(?P<diagnostico>.+)/(?P<total>.+)/$', 
        update, name='update'),
    url(r'^(?P<clave>.+)/$', read, name='read'),
]
