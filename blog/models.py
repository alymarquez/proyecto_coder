from django.db import models

# Create your models here.

class blog(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

class animal(models.Model):
    nombre = models.CharField(max_length=64)
    edad= models.IntegerField()
    tipo_de_animal = models.CharField(max_length=200)
    curiosidades = models.TextField(null= True)

    def __str__(self):
        return self.nombre


class usuario(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nombre
    