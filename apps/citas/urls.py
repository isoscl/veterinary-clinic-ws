from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', report, name='report'),
    url(r'^create/$', create, name='create'),
    url(r'^update/$', update, name='update'),
    url(r'^delete/$', delete, name='delete'),
]
