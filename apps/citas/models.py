from django.db import models


class Cita(models.Model):
    cve_cita = models.CharField(primary_key=True, max_length=18)
    fecha = models.CharField(max_length=18)
    rfc_medico = models.TextField(blank=True, null=True)
    id_mascota = models.TextField(blank=True, null=True)
    hora = models.TextField(blank=True, null=True)
    diagnostico = models.TextField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cita'
        unique_together = (('cve_cita', 'fecha'),)
