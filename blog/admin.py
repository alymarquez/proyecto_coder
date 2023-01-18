from django.contrib import admin
from .models import blog, animal, usuario


# Register your models here.

admin.site.register(blog)
admin.site.register(animal)
admin.site.register(usuario)