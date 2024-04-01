from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppCoder.models import Curso
from AppCoder.forms import Curso_formulario
from AppCoder.models import Profesor
from AppCoder.forms import Profesor_formulario
from AppCoder.models import Alumno
from AppCoder.forms import Alumno_formulario



# Create your views here.


def inicio(request):
    return render( request , "padre.html")

#def alumnos(request):
#    return render(request , "alumnos.html")



#--------------------------------------------------------------------------------------------------------#


def curso_alta(request,nombre):
    curso = Curso(nombre=nombre , camada=1322546)
    curso.save()
    texto = f"Se guardo en la base de datos el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)


def cursos_ver(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def curso_formulario(request):
    if request.method == "POST":
        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=datos["nombre"] , camada=datos["camada"])
            curso.save()
            return render(request , "curso_formulario.html")
    
    return render(request , "curso_formulario.html")


def curso_buscar(request):
    return render(request, "curso_buscar.html")


def cursobuscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render( request , "curso_resultado_busqueda.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")


def curso_elimina(request , id ):
    curso = Curso.objects.get(id=id)
    curso.delete()
    curso = Curso.objects.all()
    return render(request , "cursos.html" , {"cursos":curso})


def cursoeditar(request , id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Curso_formulario( request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()
            curso = Curso.objects.all()
            return render(request , "cursos.html" , {"cursos":curso})
        
    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre , "camada":curso.camada})
        
    return render( request , "curso_editar.html" , {"mi_formulario": mi_formulario , "curso":curso})


#--------------------------------------------------------------------------------------------------------#


def profesor_alta(request,nombre):
    profesor = Profesor(nombre=nombre , codigo=1322546)
    profesor.save()
    texto = f"Se guardo en la base de datos el profesor: {profesor.nombre} {profesor.codigo}"
    return HttpResponse(texto)


def profesores_ver(request):
    profesores = Profesor.objects.all()
    dicc = {"profesores": profesores}
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def profesor_formulario(request):
    if request.method == "POST":
        mi_formulario = Profesor_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor = Profesor( nombre=datos["nombre"] , codigo=datos["codigo"])
            profesor.save()
            return render(request , "profesor_formulario.html")
    
    return render(request , "profesor_formulario.html")


def profesor_buscar(request):
    return render(request, "profesor_buscar.html")


def profesorbuscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        profesores = Profesor.objects.filter(nombre__icontains= nombre)
        return render( request , "profesor_resultado_busqueda.html" , {"profesores":profesores})
    else:
        return HttpResponse("Ingrese el nombre del profesor")


def profesor_elimina(request , id ):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    profesor = Profesor.objects.all()
    return render(request , "profesores.html" , {"profesores":profesor})


def profesoreditar(request , id):
    profesor = Profesor.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Profesor_formulario( request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor.nombre = datos["nombre"]
            profesor.codigo = datos["codigo"]
            profesor.save()
            profesor = Profesor.objects.all()
            return render(request , "profesores.html" , {"profesores":profesor})
        
    else:
        mi_formulario = Profesor_formulario(initial={"nombre":profesor.nombre , "codigo":profesor.codigo})
        
    return render( request , "profesor_editar.html" , {"mi_formulario": mi_formulario , "profesor":profesor})


#--------------------------------------------------------------------------------------------------------#



def alumno_alta(request,nombre):
    alumno = Alumno(nombre=nombre , dni=1322546)
    alumno.save()
    texto = f"Se guardo en la base de datos el alumno: {alumno.nombre} {alumno.dni}"
    return HttpResponse(texto)


def alumnos_ver(request):
    alumnos = Alumno.objects.all()
    dicc = {"alumnos": alumnos}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def alumno_formulario(request):
    if request.method == "POST":
        mi_formulario = Alumno_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno = Alumno( nombre=datos["nombre"] , dni=datos["dni"])
            alumno.save()
            return render(request , "alumno_formulario.html")
    
    return render(request , "alumno_formulario.html")


def alumno_buscar(request):
    return render(request, "alumno_buscar.html")


def alumnobuscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        alumnos = Alumno.objects.filter(nombre__icontains= nombre)
        return render( request , "alumno_resultado_busqueda.html" , {"alumnos":alumnos})
    else:
        return HttpResponse("Ingrese el nombre del alumno")


def alumno_elimina(request , id ):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    alumno = Alumno.objects.all()
    return render(request , "alumnos.html" , {"alumnos":alumno})


def alumnoeditar(request , id):
    alumno = Alumno.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Alumno_formulario( request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno.nombre = datos["nombre"]
            alumno.dni = datos["dni"]
            alumno.save()
            alumno = Alumno.objects.all()
            return render(request , "alumnos.html" , {"alumnos":alumno})
        
    else:
        mi_formulario = Alumno_formulario(initial={"nombre":alumno.nombre , "dni":alumno.dni})
        
    return render( request , "alumno_editar.html" , {"mi_formulario": mi_formulario , "alumno":alumno})


#--------------------------------------------------------------------------------------------------------#