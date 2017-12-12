from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^citas/', include('apps.citas.urls', namespace="citas")),
    url(r'^clientes/', include('apps.clientes.urls', namespace="clientes")),
    url(r'^detalle_citas/', include('apps.detalle_citas.urls', namespace="detalle_citas")),
    url(r'^mascotas/', include('apps.mascotas.urls', namespace="mascotas")),
    url(r'^medicos/', include('apps.medicos.urls', namespace="medicos")),
    url(r'^servicios/', include('apps.servicios.urls', namespace="servicios")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
