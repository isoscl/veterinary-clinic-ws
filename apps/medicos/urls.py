from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', report, name='report'),
    url(r'^create/(?P<rfc>.+)/(?P<nombre>.+)/(?P<direccion>.+)/(?P<telefono>.+)/(?P<email>.+)/$', 
        create, name='create'),
    url(r'^(?P<rfc>.+)/$', read, name='read'),
    url(r'^(?P<rfc>.+)/update/(?P<nombre>.+)/(?P<direccion>.+)/(?P<telefono>.+)/(?P<email>.+)/$', 
        update, name='update'),
    url(r'^(?P<rfc>.+)/delete/$', delete, name='delete'),
]
