from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', report, name='report'),
    url(r'^create/(?P<cve_cita>\w+)/(?P<fecha>[\d-]+)/(?P<cve_servicio>[\w]+)/(?P<cantidad>\d+)/(?P<subtotal>\d+\.?\d+)/$', 
        create, name='create'),
    url(r'^(?P<cve_cita>\w+)/(?P<fecha>[\d-]+)/(?P<cve_servicio>[\w]+)/$', read, name='read'),
    url(r'^(?P<cve_cita>\w+)/(?P<fecha>[\d-]+)/(?P<cve_servicio>[\w]+)/update/(?P<cantidad>\d+)/(?P<subtotal>\d+\.?\d+)/$', 
        update, name='update'),
    url(r'^(?P<cve_cita>\w+)/(?P<fecha>[\d-]+)/(?P<cve_servicio>[\w]+)/delete/$', delete, name='delete'),
]
