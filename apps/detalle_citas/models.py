from django.db import models


class DetalleCita(models.Model):
    cve_cita = models.CharField(db_column='cve_cita', primary_key=True, max_length=18)
    fecha = models.TextField()
    cve_servicio = models.TextField()
    cantidad = models.IntegerField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Detalle_cita'
        unique_together = (('cve_cita', 'fecha', 'cve_servicio'),)
