from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blog.models import Avatar, animal
from django.core.files.images import get_image_dimensions

class CrearBlog(forms.Form):
    titulo = forms.CharField(label="Titulo del blog", max_length=200)
    descripcion = forms.CharField(widget=forms.Textarea)
    imagen = forms.ImageField()

class CrearAnimal(forms.Form):
    tipo_de_animal = forms.CharField(label="¿Que animal es?", max_length=200)
    edad= forms.IntegerField()
    nombre = forms.CharField(label="nombre:", max_length=200)
    curiosidades = forms.CharField(widget=forms.Textarea)
    imagen = forms.ImageField()
    email = forms.EmailField()

    class Meta:
        model = animal
        fields=('imagen')



class CrearUsuario(forms.Form):
    nombre= forms.CharField(label="nombre:", max_length="200")
    apellido = forms.CharField(max_length=200)
    dni = forms.IntegerField()
    email = forms.EmailField()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    username = forms.CharField(label="usuario")

    class Meta:
        model = User
        fields = ['username','email']



class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['imagen']