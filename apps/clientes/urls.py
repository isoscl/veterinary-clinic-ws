from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', report, name='report'),
    url(r'^create/(?P<rfc>.+)/(?P<nombre>.+)/(?P<direccion>.+)/(?P<telefono>.+)/(?P<email>.+)/$', 
        create, name='create'), # create/JFGV/fercho/calle%203/5512345678/fer@email.com/
    url(r'^(?P<rfc>.+)/delete/$', delete, name='delete'), # JFGV/delete/
    url(r'^(?P<rfc>.+)/update/(?P<nombre>.+)/(?P<direccion>.+)/(?P<telefono>.+)/(?P<email>.+)/$', 
        update, name='update'), # JFGV/update/fercho/calle%203/5512345678/fer@email.com/
    url(r'^(?P<rfc>.+)/mascotas/$', pets, name='pets'),
    url(r'^(?P<rfc>.+)/$', read, name='read'),
]
