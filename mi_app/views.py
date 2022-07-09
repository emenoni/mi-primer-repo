from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from mi_app.models import curso, Estudiante


# Create your views here.


def saludo (request):
    
    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"Hola mundo {fecha_hora_ahora}")

def saludar_a(request, nombre):
    return HttpResponse(f"Hola, cómo estas {nombre}")

def saludo_personalizado(request):
    context = {}

    if request.GET:
        context["nombre"]=request.GET["nombre"]
    return render(request, "mi_app/index.html", context)

def imc(request):
    context = {}

    if request.GET:
        context["peso","altura"] = request.GET["peso","altura"]
    
    return render(request, 'mi_app/imc.html', context)

def listar_cursos(request):
    context = {}

    context["cursos"] = curso.objects.all()

    return render(request, 'mi_app/lista_cursos.html', context)

def listar_estudiantes(request):
    context = {}
    
    context["estudiantes"] = Estudiante.objects.all()
    
    return render(request, 'mi_app/lista_estudiantes.html', context)
