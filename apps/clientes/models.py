from django.db import models


class Cliente(models.Model):
    rfc_cliente = models.CharField(primary_key=True, max_length=18)
    nombre_cliente = models.TextField(blank=True, null=True)
    direccion_cliente = models.TextField(blank=True, null=True)
    telefono_cliente = models.TextField(blank=True, null=True)
    email_cliente = models.TextField(blank=True, null=True)
    imagen_cliente = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cliente'

    def __str__(self):
        return self.nombre_cliente