from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import blog, animal, usuario
from .forms import *
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView

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
        animal.objects.create(tipo_de_animal=request.POST['tipo_de_animal'], edad=request.POST['edad'], nombre=request.POST['nombre'], curiosidades=request.POST['curiosidades'])
        return redirect('/animalitos/')


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



def register(request):
    if request.method == "POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, "index.html", {"mensaje": "usuario creado"})
        
    else:
        form = UserRegisterForm()

    return render(request, "registro.html", {"form": form})    




def login_request(request):
    if request.method== "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contraseña)


            if user:
                login(request= request, user=user)

                return render(request, "index.html")
           

    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form":form})



class CustomLogoutView(LogoutView):
    template_name = 'logout.html'
    next_page = reverse_lazy('/')



        