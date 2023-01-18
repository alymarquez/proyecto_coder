from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import blog, animal, usuario
from .forms import *



def index(request):
    return render(request, 'index.html')



def about(request):
    return render(request, 'about.html')



def blogs(request):
    blogs = blog.objects.all()
    return render(request, 'blogs.html', {
        'blogs': blogs
    })


def contenido_blog(request, id):
    contenido = get_object_or_404(blog, id=id)
    detalles = blog.objects.filter(id=id)
    return render(request, 'contenido.html', {
        'contenido': contenido,
        'detalles': detalles
        })


def crear_blogs(request):
    if request.method == 'GET':
        return render(request, 'crear_blogs.html', {'form': CrearBlog})
    
    else:
        blog.objects.create(titulo=request.POST['titulo'], descripcion=request.POST['descripcion'])
        return redirect('/blogs/')



def animalitos(request):
    animalitos = animal.objects.all()
    return render(request, 'animalitos.html', {
        'animalitos': animalitos
    })


def crear_animal(request):
    if request.method == 'GET':
        return render(request, 'crear_animales.html', {'form': CrearAnimal})
    
    else:
        animal.objects.create(animal=request.POST['animal'], nombre=request.POST['nombre'], descripcion=request.POST['descripcion'])
        return redirect('/animales/')


def tienda(request):
    return render(request, 'tienda.html')

def crear_usuario(request):
    if request.method == 'GET':
        return render(request, 'usuario.html', {'form': CrearUsuario})
    
    else:
        usuario.objects.create(nombre=request.POST['nombre'], apellido=request.POST['apellido'], dni=request.POST['dni'], email=request.POST['email'])
        return redirect('')



def buscar(request):
    if request.GET["q"]:

        q = request.GET['q']
        animales = animal.objects.filter(tipo_de_animal__icontains=q)
        return render(request, 'buscar.html',{"animales":animales})

    else: 
         respuesta = "no existen esos datos"
         
         return HttpResponse(respuesta)