from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import blog, animal, Avatar
from .forms import *
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView



def index(request):
    return render(request, 'index.html')



def about(request):
    return render(request, 'about.html')



#BLOG
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


@login_required 
def crear_blogs(request):
    if request.method == "POST":
        form = CrearBlog(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            blogs = blog(titulo=data['titulo'], descripcion=data['descripcion'], imagen=data['imagen'], owner=request.user)
            blogs.save()
            url_exitosa = reverse('blogs')
            return redirect(url_exitosa)
    else:  # GET
        form = CrearBlog()
    return render(
        request=request,
        template_name='crear_blogs.html',
        context={'form': form},
    )


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = blog
    success_url = reverse_lazy('blogs')
    template_name = 'eliminar_blog.html'

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = blog
    fields = ['titulo', 'descripcion']
    success_url = reverse_lazy('blogs')
    template_name = 'actualizar_blog.html'
        


#ADOPCION
def animalitos(request):
    animalitos = animal.objects.all()
    return render(request, 'animalitos.html', {
        'animalitos': animalitos
    })

@login_required
def crear_animal(request):
    if request.method == "POST":
        form = CrearAnimal(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            animales = animal(tipo_de_animal=data['tipo_de_animal'], edad=data['edad'], nombre=data['nombre'], curiosidades=data['curiosidades'], imagen=data['imagen'], email=data['email'])
            animales.save()
            url_exitosa = reverse('animalitos')
            return redirect(url_exitosa)
    else:  # GET
        form = CrearAnimal()

    return render(
        request=request,
        template_name='crear_animales.html',
        context={'form': form},
    )


class AnimalDetalle(DetailView):
    model = animal
    template_name = 'adopcion.html'


def buscar(request):
    if request.GET["q"]:

        q = request.GET['q']
        animales = animal.objects.filter(tipo_de_animal__icontains=q)
        return render(request, 'buscar.html',{"animales":animales})

    else: 
         respuesta = "no existen esos datos"
         
         return HttpResponse(respuesta)



def tienda(request):
    return render(request, 'tienda.html')


#REGISTER Y LOGIN
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
    next_page = reverse_lazy('')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('')
    template_name = "formulario_perfil.html"

    def get_object(self, queryset=None):
        return self.request.user



def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES) 

        if formulario.is_valid():
            avatar = formulario.save()
            avatar.user = request.user
            avatar.save()
            url_exitosa = reverse('')
            return redirect(url_exitosa)
    else: 
        formulario = AvatarFormulario()
    return render(
        request=request,
        template_name='formulario_avatar.html',
        context={'form': formulario},
    )