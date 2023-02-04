from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class blog(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='blogs', null = True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titulo

class animal(models.Model):
    nombre = models.CharField(max_length=64)
    edad= models.IntegerField()
    tipo_de_animal = models.CharField(max_length=200)
    curiosidades = models.TextField(null= True)
    imagen = models.ImageField(upload_to='animales', null = True, blank=True)
    email = models.EmailField(null = True)

    def __str__(self):
        return self.nombre



class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"Imagen de: {self.user}"



    