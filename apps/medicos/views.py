from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

from .models import Medico


@csrf_exempt
def report(request):
    if 'rfc' in request.POST:
        objects = Medico.objects.filter(rfc_medico=request.POST['rfc']).values()
    else:
        objects = Medico.objects.all().values()

    return JsonResponse({'objects': list(objects)})

@csrf_exempt
def create(request):
    rfc = request.POST['rfc']
    nombre = request.POST['nombre']
    direccion = request.POST['direccion']
    telefono = request.POST['telefono']
    email = request.POST['email']

    medico = Medico.objects.create(
        rfc_medico = rfc,
        nombre_medico = nombre,
        direccion_medico = direccion,
        telefono_medico = telefono,
        email_medico = email,
    )
    objects = Medico.objects.filter(rfc_medico=rfc).values()
    return JsonResponse({'objects': list(objects)})

@csrf_exempt
def update(request):
    rfc = request.POST['rfc']
    nombre = request.POST['nombre']
    direccion = request.POST['direccion']
    telefono = request.POST['telefono']
    email = request.POST['email']

    medico = Medico.objects.get(rfc_medico=rfc)
    medico.nombre_medico = nombre
    medico.direccion_medico = direccion
    medico.telefono_medico = telefono
    medico.email_medico = email
    medico.save()
    objects = Medico.objects.filter(rfc_medico=rfc).values()
    return JsonResponse({'objects': list(objects)})

@csrf_exempt
def delete(request):
    rfc = request.POST['rfc']
    medico = Medico.objects.get(rfc_medico=rfc).delete()
    message = {'message': 'medico eliminado'} if medico else {'message': 'No se pudo eliminar el medico'}
    return JsonResponse(message)

@csrf_exempt
def image(request):
    medico = Medico.objects.get(rfc_medico=request.POST['rfc'])
    imagen = request.FILES['imagen']
    fs = FileSystemStorage()
    filename = fs.save(imagen.name, imagen)
    medico.imagen_medico = filename
    medico.save()
    objects = Medico.objects.filter(rfc_medico=request.POST['rfc']).values()
    return JsonResponse({'objects': list(objects)})
