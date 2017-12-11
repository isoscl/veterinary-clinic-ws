from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', report, name='report'),
    url(r'^create/(?P<descripcion>.+)/(?P<precio>.+)/$', create, name='create'),
    url(r'^(?P<clave>.+)/delete/$', delete, name='delete'),
    url(r'^(?P<clave>.+)/update/(?P<descripcion>.+)/(?P<precio>.+)/$', update, name='update'),
    url(r'^(?P<clave>.+)/$', read, name='read'),
]
