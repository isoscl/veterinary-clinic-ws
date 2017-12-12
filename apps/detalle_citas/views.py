from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

from .models import DetalleCita


@csrf_exempt
def report(request):
    if ['cve_cita', 'fecha', 'cve_servicio'] in request.POST:
        detalle_citas = serializers.serialize('json', [DetalleCita.objects.get(cve_cita=cve_cita, fecha=fecha, cve_servicio=cve_servicio)])
    else:
        detalle_citas = serializers.serialize('json', DetalleCita.objects.all())

    return HttpResponse(detalle_citas, content_type='application/json')

@csrf_exempt
def create(request):
    cve_cita = request.POST['cve_cita']
    fecha = request.POST['fecha']
    cve_servicio = request.POST['cve_servicio']
    cantidad = request.POST['cantidad']
    subtotal = request.POST['subtotal']

    detalle_cita = DetalleCita.objects.create(
        cve_cita = cve_cita,
        fecha = fecha,
        cve_servicio = cve_servicio,
        cantidad = cantidad,
        subtotal = subtotal
    )
    detalle_cita = serializers.serialize('json', [detalle_cita])
    return HttpResponse(detalle_cita, content_type='application/json')

@csrf_exempt
def update(request):
    cve_cita = request.POST['cve_cita']
    fecha = request.POST['fecha']
    cve_servicio = request.POST['cve_servicio']
    cantidad = request.POST['cantidad']
    subtotal = request.POST['subtotal']

    detalle_cita = DetalleCita.objects.get(cve_cita=cve_cita, fecha=fecha, cve_servicio=cve_servicio)
    detalle_cita.cantidad = int(cantidad)
    detalle_cita.subtotal = float(subtotal)

    detalle_cita.save()
    detalle_cita = serializers.serialize('json', [detalle_cita])
    return HttpResponse(detalle_cita, content_type='application/json')

@csrf_exempt
def delete(request):
    cve_cita = request.POST['cve_cita']
    fecha = request.POST['fecha']
    cve_servicio = request.POST['cve_servicio']
    detalle_cita = DetalleCita.objects.get(cve_cita=cve_cita, fecha=fecha, cve_servicio=cve_servicio).delete()
    message = {'message': 'detalle_cita eliminado'} if detalle_cita else {'message': 'No se pudo eliminar el detalle_cita'}
    return JsonResponse(message)
