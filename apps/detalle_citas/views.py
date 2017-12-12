from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

from .models import DetalleCita


@csrf_exempt
def report(request):
    if 'cve_cita' in request.POST and 'fecha' in request.POST and 'cve_servicio' in request.POST:
        objects = DetalleCita.objects.filter(cve_cita=request.POST['cve_cita'],\
            fecha=request.POST['fecha'], cve_servicio=request.POST['cve_servicio']).values()
    else:
        objects = DetalleCita.objects.all().values()

    return JsonResponse({'objects': list(objects)})

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
    objects = DetalleCita.objects.filter(cve_cita=cve_cita,\
        fecha=fecha, cve_servicio=cve_servicio).values()
    return JsonResponse({'objects': list(objects)})

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
    objects = DetalleCita.objects.filter(cve_cita=cve_cita,\
        fecha=fecha, cve_servicio=cve_servicio).values()
    return JsonResponse({'objects': list(objects)})

@csrf_exempt
def delete(request):
    cve_cita = request.POST['cve_cita']
    fecha = request.POST['fecha']
    cve_servicio = request.POST['cve_servicio']
    detalle_cita = DetalleCita.objects.get(cve_cita=cve_cita, fecha=fecha, cve_servicio=cve_servicio).delete()
    message = {'message': 'detalle_cita eliminado'} if detalle_cita else {'message': 'No se pudo eliminar el detalle_cita'}
    return JsonResponse(message)
