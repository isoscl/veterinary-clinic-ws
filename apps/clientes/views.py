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
        clientes = serializers.serialize('json', [Cliente.objects.get(rfc_cliente=request.POST['rfc'])])
    else:
        clientes = serializers.serialize('json', Cliente.objects.all())

    return HttpResponse(clientes, content_type='application/json')

@csrf_exempt
def create(request):
    rfc = request.POST['rfc']
    nombre = request.POST['nombre']
    direccion = request.POST['direccion']
    telefono = request.POST['telefono']
    email = request.POST['email']

    if 'imagen' in request.FILES:
        imagen = request.FILES['imagen']
        fs = FileSystemStorage()
        fs.save(imagen.name, imagen)
        imagen = imagen.name
    else:
        imagen = None

    cliente = Cliente.objects.create(
        rfc_cliente = rfc,
        nombre_cliente = nombre,
        direccion_cliente = direccion,
        telefono_cliente = telefono,
        email_cliente = email,
        imagen_cliente = imagen
    )
    cliente = serializers.serialize('json', [cliente])
    return HttpResponse(cliente, content_type='application/json')

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
    
    if 'imagen' in request.FILES:
        imagen = request.FILES['imagen']
        fs = FileSystemStorage()
        fs.save(imagen.name, imagen)
        cliente.imagen_cliente = imagen.name
        
    cliente.save()
    cliente = serializers.serialize('json', [cliente])
    return HttpResponse(cliente, content_type='application/json')

@csrf_exempt
def delete(request):
    rfc = request.POST['rfc']
    cliente = Cliente.objects.get(rfc_cliente=rfc).delete()
    message = {'message': 'Cliente eliminado'} if cliente else {'message': 'No se pudo eliminar el cliente'}
    return JsonResponse(message)

@csrf_exempt
def pets(request):
    rfc = request.POST['rfc']
    pets = serializers.serialize('json', Mascota.objects.filter(rfc_cliente=rfc))
    return HttpResponse(pets, content_type='application/json')
