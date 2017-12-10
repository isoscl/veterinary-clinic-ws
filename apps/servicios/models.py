from django.db import models


class Servicio(models.Model):
    cve_servicio = models.CharField(primary_key=True, max_length=18)
    descripcion_servicio = models.TextField(blank=True, null=True)
    precio_servicio = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Servicio'
