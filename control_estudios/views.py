from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView #no los uso
from django.db.models import Q #no lo uso

from control_estudios.models import Curso, Estudiante, Profesor
from control_estudios.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario

#Vistas relativas a la app
# Vistas de cursos
def listar_cursos(request):
    contexto = {
        "cursos": Curso.objects.all(), #hago dinamica la base de datos
    }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_cursos.html',
        context=contexto,
    )
    return http_response

def crear_curso(request):
    if request.method == "POST":
        # Creo un objeto formulario con la data que envio el usuario
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            comision = data["comision"]
            # creo un curso en memoria RAM
            curso = Curso(nombre=nombre, comision=comision)
            # Lo guardan en la Base de datos
            curso.save()

            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('lista_cursos')  # estudios/cursos/
            return redirect(url_exitosa)
    else:  # GET
        formulario = CursoFormulario()
    http_response = render(
        request=request,
        template_name='control_estudios/formulario_curso.html',
        context={'formulario': formulario}
    )
    return http_response

def buscar_cursos(request):
   if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        cursos = Curso.objects.filter(comision__contains=busqueda)
        
        contexto = {
            "cursos": cursos,
        }
        http_response = render(
            request=request,
            template_name='control_estudios/lista_cursos.html',
            context=contexto,
        )
        return http_response

def eliminar_curso(request, id):
    # obtienes el curso de la base de datos
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        # borra el curso de la base de datos
        curso.delete()
        # redireccionamos a la URL exitosa
        url_exitosa = reverse('lista_cursos')
        return redirect(url_exitosa)

def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso.nombre = data['nombre']
            curso.comision = data['comision']
            curso.save()

            url_exitosa = reverse('lista_cursos')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'nombre': curso.nombre,
            'comision': curso.comision,
        }
        formulario = CursoFormulario(initial=inicial)
    return render(
        request=request,
        template_name='control_estudios/formulario_curso.html',
        context={'formulario': formulario},
    )

def listar_estudiantes(request):
    contexto = {
        "estudiantes": Estudiante.objects.all(), #hago dinamica la base de datos, puede haber datos constantes
    }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_estudiantes.html',
        context=contexto,
    )
    return http_response


def crear_estudiante(request):
    if request.method == "POST":
        
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  
            nombre = data["nombre"]
            apellido = data["apellido"]
            dni = data["dni"]
            email = data["email"]
            telefono = data["telefono"]
            fecha_nacimiento = data["fecha_nacimiento"]
            # creo un estudiante en memoria RAM
            estudiante = Estudiante(nombre=nombre, apellido=apellido, dni=dni, email=email, telefono=telefono, fecha_nacimiento=fecha_nacimiento)
            
            estudiante.save()

            url_exitosa = reverse('lista_estudiantes')  # estudios/estudiantes/
            return redirect(url_exitosa)
    else:  # GET
        formulario = EstudianteFormulario()
    http_response = render(
        request=request,
        template_name='control_estudios/formulario_estudiante.html',
        context={'formulario': formulario}
    )
    return http_response

#def eliminar_estudiante(request, id):
#    # obtienes el curso de la base de datos
#    estudiante = Estudiante.objects.get(id=id)
#    if request.method == "POST":
#        # borra el curso de la base de datos
#        estudiante.delete()
#        # redireccionamos a la URL exitosa
#        url_exitosa = reverse('lista_estudiantes')
#        return redirect(url_exitosa)

#def editar_estudiante(request, id):
#    estudiante = Estudiante.objects.get(id=id)
#    if request.method == "POST":
#        formulario = EstudianteFormulario(request.POST)

#        if formulario.is_valid():
 #           data = formulario.cleaned_data
#            estudiante.nombre = data['nombre']
#            estudiante.apellido = data['apellido']
#            estudiante.save()

#            url_exitosa = reverse('lista_estudiantes')
#            return redirect(url_exitosa)
#    else:  # GET
#        inicial = {
#            'nombre': estudiante.nombre,
#            'apellido': estudiante.apellido,
#        }
#        formulario = EstudianteFormulario(initial=inicial)
#    return render(
#        request=request,
#        template_name='control_estudios/formulario_estudiante.html',
#        context={'formulario': formulario},
#    )

# Vistas de profesores
def listar_profesores(request):
    contexto = {
        "profesores": Profesor.objects.all(), #hago dinamica la base de datos, puede haber datos constantes
    }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_profesores.html',
        context=contexto,
    )
    return http_response

def crear_profesor(request):
    if request.method == "POST":
        # Creo un objeto formulario con la data que envio el usuario
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            apellido = data["apellido"]
            dni = data["dni"]
            email = data["email"]
            fecha_nacimiento = data["fecha_nacimiento"]
            profesion = data["profesion"]
            
            # creo un estudiante en memoria RAM
            profesor = Profesor(nombre=nombre, apellido=apellido, dni=dni, email=email, fecha_nacimiento=fecha_nacimiento, profesion=profesion)
            
            profesor.save()

            url_exitosa = reverse('lista_profesores')  # estudios/estudiantes/
            return redirect(url_exitosa)
    else:  # GET
        formulario = ProfesorFormulario()
    http_response = render(
        request=request,
        template_name='control_estudios/formulario_profesor.html',
        context={'formulario': formulario}
    )
    return http_response
