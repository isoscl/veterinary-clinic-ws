from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from .models import Cliente


def report(request):
    clientes = serializers.serialize('json', Cliente.objects.all())
    return HttpResponse(clientes, content_type='application/json')

def create(request, rfc, nombre, direccion, telefono, email):
    cliente = Cliente.objects.create(
        rfc_cliente = rfc,
        nombre_cliente = nombre,
        direccion_cliente = direccion,
        telefono_cliente = telefono,
        email_cliente = email
    )
    cliente = serializers.serialize('json', [cliente])
    return HttpResponse(cliente, content_type='application/json')

def read(request, rfc):
    cliente = serializers.serialize('json', [Cliente.objects.get(rfc_cliente=rfc)])
    return HttpResponse(cliente, content_type='application/json')

def update(request, rfc, nombre, direccion, telefono, email):
    cliente = Cliente.objects.get(rfc_cliente=rfc)
    cliente.nombre_cliente = nombre
    cliente.direccion_cliente = direccion
    cliente.telefono_cliente = telefono
    cliente.email_cliente = email
    cliente.save()
    cliente = serializers.serialize('json', [cliente])
    return HttpResponse(cliente, content_type='application/json')

def delete(request, rfc):
    cliente = Cliente.objects.get(rfc_cliente=rfc).delete()
    message = {'message': 'Cliente eliminado'} if cliente else {'message': 'No se pudo eliminar el cliente'}
    return JsonResponse(message)
