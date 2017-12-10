from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', report, name='report'),
    url(r'^create/(?P<rfc>\w+)/(?P<nombre>[\w\s]+)/(?P<direccion>[\w\s]+)/(?P<telefono>\d+)/(?P<email>[\w@\.]+)/$', create, name='create'),
    url(r'^(?P<rfc>\w+)/$', read, name='read'),
    url(r'^(?P<rfc>\w+)/update/(?P<nombre>[\w\s]+)/(?P<direccion>[\w\s]+)/(?P<telefono>\d+)/(?P<email>[\w@\.]+)/$', update, name='update'),
    url(r'^(?P<rfc>\w+)/delete/$', delete, name='delete'),
]
