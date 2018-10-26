from django.db import models

# Create your models here.


class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Resultado(models.Model):
    alumno = models.ForeignKey(Alumno, related_name='resultado', on_delete=models.CASCADE)
    empresa = models.CharField(max_length=100)
    tiempo = models.IntegerField()
    comentarios = models.CharField(max_length=100)
