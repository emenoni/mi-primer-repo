from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.


def saludo (request):
    
    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"Hola mundo {fecha_hora_ahora}")

def saludar_a(request, nombre):
    return HttpResponse(f"Hola, cómo estas {nombre}")

def saludo_personalizado(request):
    context = {}
    return render(request, "mi_app/index.html", context)

