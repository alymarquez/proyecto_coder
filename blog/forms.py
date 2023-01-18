from django import forms

class CrearBlog(forms.Form):
    titulo = forms.CharField(label="Titulo del blog", max_length=200)
    descripcion = forms.CharField(widget=forms.Textarea)

class CrearAnimal(forms.Form):
    tipo_de_animal = forms.CharField(label="¿Que animal es?", max_length=200)
    nombre = forms.CharField(label="nombre:", max_length=200)
    curiosidades = forms.CharField(widget=forms.Textarea)

class CrearUsuario(forms.Form):
    nombre= forms.CharField(label="nombre:", max_length="200")
    apellido = forms.CharField(max_length=200)
    dni = forms.IntegerField()
    email = forms.EmailField()