from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=""),
    path('about/', views.about, name="about"),
    path('blogs/', views.blogs, name="blogs"),
    path('blogs/<int:id>', views.contenido_blog, name="contenido_blog"),
    path('animalitos/', views.animalitos, name="animalitos"),
    path('crear blogs/', views.crear_blogs, name="crear blogs"),
    path('registra tu mascota/', views.crear_animal, name="registra tu mascota"),
    path('registro/', views.crear_usuario, name= "registro"),
    path('tienda/', views.tienda, name= "tienda"),
    path('animalitos/buscar/', views.buscar, name= "buscar"),
    path('login', views.login_request, name="login"),
    path('register', views.register, name='register'),
    path('logout', views.CustomLogoutView.as_view(), name='logout')

]