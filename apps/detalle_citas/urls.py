from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', report, name='report'),
    url(r'^create/(?P<cve_cita>[^/]+)/(?P<fecha>[^/]+)/(?P<cve_servicio>[^/]+)/(?P<cantidad>[^/]+)/(?P<subtotal>[^/]+)/$', 
        create, name='create'),
    url(r'^(?P<cve_cita>[^/]+)/(?P<fecha>[^/]+)/(?P<cve_servicio>[^/]+)/delete/$', delete, name='delete'),
    url(r'^(?P<cve_cita>[^/]+)/(?P<fecha>[^/]+)/(?P<cve_servicio>[^/]+)/update/(?P<cantidad>[^/]+)/(?P<subtotal>[^/]+)/$', 
        update, name='update'),
    url(r'^(?P<cve_cita>[^/]+)/(?P<fecha>[^/]+)/(?P<cve_servicio>[^/]+)/$', read, name='read'),
]
