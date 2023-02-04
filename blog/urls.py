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
    path('tienda/', views.tienda, name= "tienda"),
    path('animalitos/buscar/', views.buscar, name= "buscar"),
    path('login', views.login_request, name="login"),
    path('register', views.register, name='register'),
    path('logout', views.CustomLogoutView.as_view(), name='logout'),
    path('editar-perfil/', views.ProfileUpdateView.as_view(), name='editar perfil'),
    path('agregar_avatar/', views.agregar_avatar, name="agregar_avatar"),
    path(r'^(?P<pk>\d+)$', views.AnimalDetalle.as_view(), name = 'adoptar'),
    path(r'^borrar/(?P<pk>\d+)$', views.BlogDeleteView.as_view(), name="eliminar blog"),
    path(r'^editar/(?P<pk>\d+)$', views.BlogUpdateView.as_view(), name="editar blog")

]