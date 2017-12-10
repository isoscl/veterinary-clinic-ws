# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DetalleCita(models.Model):
    cve_cita = models.ForeignKey(Cita, models.DO_NOTHING, db_column='cve_cita', primary_key=True)
    fecha = models.ForeignKey(Cita, models.DO_NOTHING, db_column='fecha')
    cve_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='cve_servicio')
    cantidad = models.IntegerField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Detalle_cita'
        unique_together = (('cve_cita', 'fecha', 'cve_servicio'),)

