from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from .models import Servicio


def report(request):
    servicios = serializers.serialize('json', Servicio.objects.all())
    return HttpResponse(servicios, content_type='application/json')

def create(request, clave, descripcion, precio):
    servicio = Servicio.objects.create(
        cve_servicio = clave,
        descripcion_servicio = descripcion,
        precio_servicio = precio,
    )
    servicio = serializers.serialize('json', [servicio])
    return HttpResponse(servicio, content_type='application/json')

def read(request, clave):
    servicio = serializers.serialize('json', [Servicio.objects.get(cve_servicio=clave)])
    return HttpResponse(servicio, content_type='application/json')

def update(request, clave, descripcion, precio):
    servicio = Servicio.objects.get(cve_servicio=clave)
    servicio.descripcion_servicio = descripcion
    servicio.precio_servicio = precio
    servicio.save()
    servicio = serializers.serialize('json', [servicio])
    return HttpResponse(servicio, content_type='application/json')

def delete(request, clave):
    servicio = Servicio.objects.get(cve_servicio=clave).delete()
    message = {'message': 'servicio eliminado'} if servicio else {'message': 'No se pudo eliminar el servicio'}
    return JsonResponse(message)
