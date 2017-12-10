from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', report, name='report'),
    url(r'^create/(?P<id>.+)/(?P<rfc>.+)/(?P<nombre>.+)/(?P<especie>.+)/(?P<raza>.+)/(?P<color>.+)/(?P<tamanio>.+)/(?P<senia>.+)/(?P<fecha>.+)/$', 
        create, name='create'),
    url(r'^(?P<id>.+)/$', read, name='read'),
    url(r'^(?P<id>.+)/update/(?P<rfc>.+)/(?P<nombre>.+)/(?P<especie>.+)/(?P<raza>.+)/(?P<color>.+)/(?P<tamanio>.+)/(?P<senia>.+)/(?P<fecha>.+)/$', 
        update, name='update'),
    url(r'^(?P<id>.+)/delete/$', delete, name='delete'),
]
