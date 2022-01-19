from django.db import models

# Create your models here.


class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)


class Tarea (models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    fechaInicio = models.DateTimeField()
    fechaFin = models.DateTimeField()
    estado = models.CharField(max_length=200)
    prioridad = models.IntegerField()
