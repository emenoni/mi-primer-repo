from django.contrib import admin
from django.urls import path
from mi_app.models import curso
from mi_app.views import imc, saludar_a, saludo, saludo_personalizado, listar_cursos, listar_estudiantes

urlpatterns = [
    path('hola/', saludo),
    path('saludar/persona/<nombre>', saludar_a),
    path('saludoper/', saludo_personalizado),
    path('imc/', imc),
    path('mis_cursos/', listar_cursos),
    path('listar-estudiantes/', listar_estudiantes),

]
