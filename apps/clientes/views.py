from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

from apps.mascotas.models import Mascota
from .models import Cliente


@csrf_exempt
def report(request):
    if 'rfc' in request.POST:
        objects = Cliente.objects.filter(rfc_cliente=request.POST['rfc']).values()
        return JsonResponse({'objects': list(objects)})
    else:
        objects = Cliente.objects.all().values()
        return JsonResponse({'objects': list(objects)})

@csrf_exempt
def create(request):
    rfc = request.POST['rfc']
    nombre = request.POST['nombre']
    direccion = request.POST['direccion']
    telefono = request.POST['telefono']
    email = request.POST['email']

    cliente = Cliente.objects.create(
        rfc_cliente = rfc,
        nombre_cliente = nombre,
        direccion_cliente = direccion,
        telefono_cliente = telefono,
        email_cliente = email,
    )
    objects = Cliente.objects.filter(rfc_cliente=rfc).values()
    return JsonResponse({'objects': list(objects)})

@csrf_exempt
def update(request):
    rfc = request.POST['rfc']
    nombre = request.POST['nombre']
    direccion = request.POST['direccion']
    telefono = request.POST['telefono']
    email = request.POST['email']

    cliente = Cliente.objects.get(rfc_cliente=rfc)
    cliente.nombre_cliente = nombre
    cliente.direccion_cliente = direccion
    cliente.telefono_cliente = telefono
    cliente.email_cliente = email
    cliente.save()
    objects = Cliente.objects.filter(rfc_cliente=rfc).values()
    return JsonResponse({'objects': list(objects)})

@csrf_exempt
def delete(request):
    rfc = request.POST['rfc']
    cliente = Cliente.objects.get(rfc_cliente=rfc).delete()
    message = {'message': 'Cliente eliminado'} if cliente else {'message': 'No se pudo eliminar el cliente'}
    return JsonResponse(message)

@csrf_exempt
def pets(request):
    objects = Mascota.objects.filter(rfc_cliente=request.POST['rfc']).values()
    return JsonResponse({'objects': list(objects)})

@csrf_exempt
def image(request):
    cliente = Cliente.objects.get(rfc_cliente=request.POST['rfc'])
    imagen = request.FILES['imagen']
    fs = FileSystemStorage()
    filename = fs.save(imagen.name, imagen)
    cliente.imagen_cliente = filename
    cliente.save()
    objects = Cliente.objects.filter(rfc_cliente=request.POST['rfc']).values()
    return JsonResponse({'objects': list(objects)})
