from django.urls import path
from . import views

urlpatterns = [
    path("" , views.inicio , name="home"),
#    path("alumnos", views.alumnos , name="alumnos"),
    path("cursos_ver", views.cursos_ver , name="cursos"),
    path("curso_alta", views.curso_formulario),
    path("curso_buscar", views.curso_buscar),
    path("cursobuscar", views.cursobuscar),
    path("curso_elimina/<int:id>" , views.curso_elimina , name="curso_elimina"),
    path("curso_editar/<int:id>" , views.cursoeditar , name="curso_editar"),
#
    path("profesores_ver", views.profesores_ver , name="profesores"),
    path("profesor_alta", views.profesor_formulario),
    path("profesor_buscar", views.profesor_buscar),
    path("profesorbuscar", views.profesorbuscar),
    path("profesor_elimina/<int:id>" , views.profesor_elimina , name="profesor_elimina"),
    path("profesor_editar/<int:id>" , views.profesoreditar , name="profesor_editar"),
#  
    path("alumnos_ver", views.alumnos_ver , name="alumnos"),
    path("alumno_alta", views.alumno_formulario),
    path("alumno_buscar", views.alumno_buscar),
    path("alumnobuscar", views.alumnobuscar),
    path("alumno_elimina/<int:id>" , views.alumno_elimina , name="alumno_elimina"),
    path("alumno_editar/<int:id>" , views.alumnoeditar , name="alumno_editar")
    
]