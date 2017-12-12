from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

from .models import Cita


@csrf_exempt
def report(request):
    if 'cve' in request.POST:
        citas = serializers.serialize('json', [Cita.objects.get(cve_cita=request.POST['cve'])])
    else:
        citas = serializers.serialize('json', Cita.objects.all())

    return HttpResponse(citas, content_type='application/json')

@csrf_exempt
def create(request):
    try: 
        citas = Cita.objects.all()
        ultima_cita = citas[len(citas)-1]
        tabla, numero = ultima_cita.pk.split('_')
        cve = '_'.join((tabla, str(int(numero) + 1)))
    except:
        cve = 'cita_1'

    fecha = request.POST['fecha']
    rfc = request.POST['rfc']
    id = request.POST['id']
    hora = request.POST['hora']
    diagnostico = request.POST['diagnostico']
    total = request.POST['total']

    cita = Cita.objects.create(
        cve_cita = cve,
        fecha = fecha,
        rfc_medico = rfc,
        id_mascota = id,
        hora = hora,
        diagnostico = diagnostico,
        total = total
    )
    cita = serializers.serialize('json', [cita])
    return HttpResponse(cita, content_type='application/json')

@csrf_exempt
def update(request):
    cve = request.POST['cve']
    fecha = request.POST['fecha']
    rfc = request.POST['rfc']
    id = request.POST['id']
    hora = request.POST['hora']
    diagnostico = request.POST['diagnostico']
    total = request.POST['total']

    cita = Cita.objects.get(cve_cita=cve)
    cita.fecha = fecha
    cita.rfc_medico = rfc
    cita.id_mascota = id
    cita.hora = hora
    cita.diagnostico = diagnostico
    cita.total = float(total)

    cita.save()
    cita = serializers.serialize('json', [cita])
    return HttpResponse(cita, content_type='application/json')

@csrf_exempt
def delete(request):
    cve = request.POST['cve']
    cita = Cita.objects.get(cve_cita=cve).delete()
    message = {'message': 'cita eliminado'} if cita else {'message': 'No se pudo eliminar el cita'}
    return JsonResponse(message)
