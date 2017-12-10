from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from .models import Cita


def report(request):
    citas = serializers.serialize('json', Cita.objects.all())
    return HttpResponse(citas, content_type='application/json')

def create(request, clave, fecha, rfc, id, hora, diagnostico, total):
    cita = Cita.objects.create(
        cve_cita = clave,
        fecha = fecha,
        rfc_medico = rfc,
        id_mascota = id,
        hora = hora,
        diagnostico = diagnostico,
        total = total,
    )
    cita = serializers.serialize('json', [cita])
    return HttpResponse(cita, content_type='application/json')

def read(request, clave):
    cita = serializers.serialize('json', [Cita.objects.get(cve_cita=clave)])
    return HttpResponse(cita, content_type='application/json')

def update(request, clave, fecha, rfc, id, hora, diagnostico, total):
    cita = Cita.objects.get(cve_cita=clave)
    cita.fecha = fecha
    cita.rfc_medico = rfc
    cita.id_mascota = id
    cita.hora = hora
    cita.diagnostico = diagnostico
    cita.total = float(total)
    cita.save()
    cita = serializers.serialize('json', [cita])
    return HttpResponse(cita, content_type='application/json')

def delete(request, clave):
    cita = Cita.objects.get(cve_cita=clave).delete()
    message = {'message': 'cita eliminado'} if cita else {'message': 'No se pudo eliminar el cita'}
    return JsonResponse(message)
