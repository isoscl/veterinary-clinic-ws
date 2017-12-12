from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

from apps.citas.models import Cita
from .models import Mascota


@csrf_exempt
def report(request):
    if 'id' in request.POST:
        mascotas = serializers.serialize('json', [Mascota.objects.get(id_mascota=request.POST['id'])])
    else:
        mascotas = serializers.serialize('json', Mascota.objects.all())

    return HttpResponse(mascotas, content_type='application/json')

@csrf_exempt
def create(request):
    id = request.POST['id']
    rfc = request.POST['rfc']
    nombre = request.POST['nombre']
    especie = request.POST['especie']
    raza = request.POST['raza']
    color = request.POST['color']
    tamanio = request.POST['tamanio']
    senia = request.POST['senia']
    fecha = request.POST['fecha']

    mascota = Mascota.objects.create(
        id_mascota = id,
        nombre_mascota = nombre,
        especie_mascota = especie,
        raza_mascota = raza,
        color_mascota = color,
        tamaño_mascota = tamanio,
        señapart_mascota = senia,
        fechanac_mascota = fecha,
        imagen_mascota = imagen
    )
    mascota = serializers.serialize('json', [mascota])
    return HttpResponse(mascota, content_type='application/json')

@csrf_exempt
def update(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    especie = request.POST['especie']
    raza = request.POST['raza']
    color = request.POST['color']
    tamanio = request.POST['tamanio']
    senia = request.POST['senia']
    fecha = request.POST['fecha']

    mascota = Mascota.objects.get(id_mascota=id)
    mascota.nombre_mascota = nombre
    mascota.especie_mascota = especie
    mascota.raza_mascota = raza
    mascota.color_mascota = color
    mascota.tamaño_mascota = tamanio
    mascota.señapart_mascota = senia
    mascota.fechanac_mascota = fecha
    mascota.save()
    mascota = serializers.serialize('json', [mascota])
    return HttpResponse(mascota, content_type='application/json')

@csrf_exempt
def delete(request):
    id = request.POST['id']
    mascota = Mascota.objects.get(id_mascota=id).delete()
    message = {'message': 'mascota eliminado'} if mascota else {'message': 'No se pudo eliminar el mascota'}
    return JsonResponse(message)

@csrf_exempt
def record(request, id):
    id = request.POST['id']
    record = serializers.serialize('json', Cita.objects.filter(id_mascota=id))
    return HttpResponse(record, content_type='application/json')

@csrf_exempt
def image(request):
    mascota = Mascota.objects.get(id_mascota=request.POST['rfc'])
    imagen = request.FILES['imagen']
    fs = FileSystemStorage()
    filename = fs.save(imagen.name, imagen)
    mascota.imagen_mascota = filename
    mascota.save()
    mascota = serializers.serialize('json', [mascota])
    return HttpResponse(mascota, content_type='application/json')
