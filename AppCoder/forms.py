from django import forms


class Curso_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()
    
    
class Profesor_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    codigo = forms.IntegerField()
    
    
class Alumno_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    dni = forms.IntegerField()