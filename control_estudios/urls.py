from django.contrib import admin
from django.urls import path

from control_estudios.views import (
    listar_cursos, crear_curso, buscar_cursos, eliminar_curso, editar_curso,
    listar_estudiantes, crear_estudiante, #eliminar_estudiante, editar_estudiante,
    listar_profesores, crear_profesor
)

# Son las URLS especificas de la app
urlpatterns = [
    # URLS de cursos
    path("cursos/", listar_cursos, name="lista_cursos"),
    path("crear-curso/", crear_curso, name="crear_curso"),
    path("buscar-cursos/", buscar_cursos, name="buscar_cursos"),
    path("editar-curso/<int:id>/", editar_curso, name="editar_curso"),
    path('eliminar-curso/<int:id>/', eliminar_curso, name="eliminar_curso"),
    # URLS de estudiantes
    path("estudiantes/", listar_estudiantes, name="lista_estudiantes"),
    path('crear-estudiante/', crear_estudiante, name="crear_estudiante"),
    #path('editar-estudiante/<int:pk>/', editar_estudiante, name="editar_estudiante"),
    #path('eliminar-estudiante/<int:pk>/', eliminar_estudiante, name="eliminar_estudiante"),
    # URLS de profesores
    path("profesores/", listar_profesores, name="lista_profesores"),
    path('crear-profesor/', crear_profesor, name="crear_profesor"),
]