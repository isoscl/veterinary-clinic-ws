from django.db import models


class Mascota(models.Model):
    id_mascota = models.CharField(primary_key=True, max_length=18)
    rfc_cliente = models.TextField(blank=True, null=True)
    nombre_mascota = models.TextField(blank=True, null=True)
    especie_mascota = models.TextField(blank=True, null=True)
    raza_mascota = models.TextField(blank=True, null=True)
    color_mascota = models.TextField(blank=True, null=True)
    tamaño_mascota = models.TextField(blank=True, null=True)
    señapart_mascota = models.TextField(blank=True, null=True)
    fechanac_mascota = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Mascota'
