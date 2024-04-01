from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    filial_asociada = models.CharField(max_length=100)

class Filial(models.Model):
    nombre_filial = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

