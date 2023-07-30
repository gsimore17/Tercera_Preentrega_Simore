from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=64)
    comision = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.comision}"


class Estudiante(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    dni = models.IntegerField()
    email = models.EmailField(blank=True)
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateField(null=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}, {self.dni}, {self.email}, {self.telefono}, {self.fecha_nacimiento}"

class Profesor(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField(blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    profesion = models.CharField(max_length=128)
    

    def __str__(self):
        return f"{self.apellido}, {self.nombre}, {self.dni}, {self.email}, {self.fecha_nacimiento}, {self.profesion}"

