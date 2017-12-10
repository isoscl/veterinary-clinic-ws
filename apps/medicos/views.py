from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from .models import Medico


def report(request):
    medicos = serializers.serialize('json', Medico.objects.all())
    return HttpResponse(medicos, content_type='application/json')

def create(request, rfc, nombre, direccion, telefono, email):
    medico = Medico.objects.create(
        rfc_medico = rfc,
        nombre_medico = nombre,
        direccion_medico = direccion,
        telefono_medico = telefono,
        email_medico = email
    )
    medico = serializers.serialize('json', [medico])
    return HttpResponse(medico, content_type='application/json')

def read(request, rfc):
    medico = serializers.serialize('json', [Medico.objects.get(rfc_medico=rfc)])
    return HttpResponse(medico, content_type='application/json')

def update(request, rfc, nombre, direccion, telefono, email):
    medico = Medico.objects.get(rfc_medico=rfc)
    medico.nombre_medico = nombre
    medico.direccion_medico = direccion
    medico.telefono_medico = telefono
    medico.email_medico = email
    medico.save()
    medico = serializers.serialize('json', [medico])
    return HttpResponse(medico, content_type='application/json')

def delete(request, rfc):
    medico = Medico.objects.get(rfc_medico=rfc).delete()
    message = {'message': 'medico eliminado'} if medico else {'message': 'No se pudo eliminar el medico'}
    return JsonResponse(message)
