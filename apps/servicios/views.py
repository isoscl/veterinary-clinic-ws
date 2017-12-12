from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

from .models import Servicio


@csrf_exempt
def report(request):
    if 'cve' in request.POST:
        objects = Servicio.objects.filter(cve_servicio=request.POST['cve']).values()
    else:
        objects = Servicio.objects.all().values()

    return JsonResponse({'objects': list(objects)})

@csrf_exempt
def create(request):
    try: 
        servicios = Servicio.objects.all()
        ultimo_servicio = servicios[len(servicios)-1]
        tabla, numero = ultimo_servicio.pk.split('_')
        cve = '_'.join((tabla, str(int(numero) + 1)))
    except:
        cve = 'servicio_1'

    descripcion = request.POST['descripcion']
    precio = request.POST['precio']

    servicio = Servicio.objects.create(
        cve_servicio = cve,
        descripcion_servicio = descripcion,
        precio_servicio = precio,
    )
    objects = Servicio.objects.filter(cve_servicio=cve).values()
    return JsonResponse({'objects': list(objects)})

@csrf_exempt
def update(request):
    cve = request.POST['cve']
    descripcion = request.POST['descripcion']
    precio = request.POST['precio']

    servicio = Servicio.objects.get(cve_servicio=cve)
    servicio.descripcion_servicio = descripcion
    servicio.precio_servicio = precio
    servicio.save()
    objects = Servicio.objects.filter(cve_servicio=cve).values()
    return JsonResponse({'objects': list(objects)})

@csrf_exempt
def delete(request):
    cve = request.POST['cve']
    servicio = Servicio.objects.get(cve_servicio=cve).delete()
    message = {'message': 'servicio eliminado'} if servicio else {'message': 'No se pudo eliminar el servicio'}
    return JsonResponse(message)

@csrf_exempt
def image(request):
    servicio = Servicio.objects.get(cve_servicio=request.POST['cve'])
    imagen = request.FILES['imagen']
    fs = FileSystemStorage()
    filename = fs.save(imagen.name, imagen)
    servicio.imagen_servicio = filename
    servicio.save()
    sobjects = Servicio.objects.filter(cve_servicio=request.POST['cve']).values()
    return JsonResponse({'objects': list(objects)})
