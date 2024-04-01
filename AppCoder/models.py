from django.db import models

# Create your models here.


class Curso(models.Model):
    
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} {self.camada}"
    
    
class Profesor(models.Model):
    
    nombre = models.CharField(max_length=40)
    codigo = models.IntegerField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} {self.codigo}"
    
    
class Alumno(models.Model):
    
    nombre = models.CharField(max_length=40)
    dni = models.IntegerField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} {self.dni}"