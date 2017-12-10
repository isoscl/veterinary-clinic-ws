from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from .models import DetalleCita


def report(request):
    detalle_citas = serializers.serialize('json', DetalleCita.objects.all())
    return HttpResponse(detalle_citas, content_type='application/json')

def create(request, cve_cita, fecha, cve_servicio, cantidad, subtotal):
    detalle_cita = DetalleCita.objects.create(
        cve_cita = cve_cita,
        fecha = fecha,
        cve_servicio = cve_servicio,
        cantidad = cantidad,
        subtotal = subtotal,
    )
    detalle_cita = serializers.serialize('json', [detalle_cita])
    return HttpResponse(detalle_cita, content_type='application/json')

def read(request, cve_cita, fecha, cve_servicio):
    detalle_cita = serializers.serialize('json', 
        [DetalleCita.objects.get(cve_cita=cve_cita, fecha=fecha, cve_servicio=cve_servicio)])
    return HttpResponse(detalle_cita, content_type='application/json')

def update(request, cve_cita, fecha, cve_servicio, cantidad, subtotal):
    detalle_cita = DetalleCita.objects.get(cve_cita=cve_cita, fecha=fecha, cve_servicio=cve_servicio)
    detalle_cita.cantidad = int(cantidad)
    detalle_cita.subtotal = float(subtotal)
    detalle_cita.save()
    detalle_cita = serializers.serialize('json', [detalle_cita])
    return HttpResponse(detalle_cita, content_type='application/json')

def delete(request, cve_cita, fecha, cve_servicio):
    detalle_cita = DetalleCita.objects.get(cve_cita=cve_cita, fecha=fecha, cve_servicio=cve_servicio).delete()
    message = {'message': 'detalle_cita eliminado'} if detalle_cita else {'message': 'No se pudo eliminar el detalle_cita'}
    return JsonResponse(message)
