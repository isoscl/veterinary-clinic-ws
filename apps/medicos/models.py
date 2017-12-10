from django.db import models


class Medico(models.Model):
    rfc_medico = models.CharField(primary_key=True, max_length=18)
    nombre_medico = models.TextField(blank=True, null=True)
    direccion_medico = models.TextField(blank=True, null=True)
    telefono_medico = models.TextField(blank=True, null=True)
    email_medico = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Medico'
