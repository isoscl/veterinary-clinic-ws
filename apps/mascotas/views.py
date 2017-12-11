from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from .models import Mascota


def report(request):
    mascotas = serializers.serialize('json', Mascota.objects.all())
    return HttpResponse(mascotas, content_type='application/json')

def create(request, id, rfc, nombre, especie, raza, color, tamanio, senia, fecha):
    mascota = Mascota.objects.create(
        rfc_cliente = rfc,
        id_mascota = id,
        nombre_mascota = nombre,
        especie_mascota = especie,
        raza_mascota = raza,
        color_mascota = color,
        tamaño_mascota = tamanio,
        señapart_mascota = senia,
        fechanac_mascota = fecha
    )
    mascota = serializers.serialize('json', [mascota])
    return HttpResponse(mascota, content_type='application/json')

def read(request, id):
    mascota = serializers.serialize('json', [Mascota.objects.get(id_mascota=id)])
    return HttpResponse(mascota, content_type='application/json')

def update(request, id, nombre, especie, raza, color, tamanio, senia, fecha):
    mascota = Mascota.objects.get(id_mascota=id)
    mascota.nombre_mascota = nombre
    mascota.especie_mascota = especie
    mascota.raza_mascota = raza
    mascota.color_mascota = color
    mascota.tamaño_mascota = tamanio
    mascota.señapart_mascota = senia
    mascota.fechanac_mascota = fecha
    mascota.save()
    mascota = serializers.serialize('json', [mascota])
    return HttpResponse(mascota, content_type='application/json')

def delete(request, id):
    mascota = Mascota.objects.get(id_mascota=id).delete()
    message = {'message': 'mascota eliminado'} if mascota else {'message': 'No se pudo eliminar el mascota'}
    return JsonResponse(message)
