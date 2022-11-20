from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PasswordChangeView


urlpatterns = [
    path('', views.hello, name=''),
    path('registrar/', views.registrar, name='registrar'), #el name=registrar se hace por si se quiere cambiar el nombre del path no habrá que cambiar todo el proyecto.
    path('peliculas/', views.peliculas, name='peliculas'),
    path('musica/', views.musica, name='musica'),
    path('suscripciones/', views.suscripcion, name='suscripciones'),
    path('user/edit/<int:id>',views.UpateUserView,name='editarUsuario'),
    #path('user/edit/<int:id>',views.UpdateUserView.as_view(),name='editarUsuario'),
    #path('password/',auth_views.PasswordChangeView.as_view(template_name="change_password.html")),
    path('user/password/',PasswordChangeView.as_view(template_name="change_password.html")),
    #path('user/password/<int:id>',views.UpatePasswordView),
    path('user/details',views.OneUserDetails,name='userdetails'),
    path('user/sent/',views.GetId,name='userdetailssent'),
    path('user/details/<int:id>',views.UserDetails,name='userdetailprofile'),
    #path('user/details/<int:id>',views.OneUserDetails,name='userdetails')

    #Busqueda producto ------------------------------
    path('buscar-pelicula/', views.buscarPelicula.as_view(), name='buscar_pelicula'),
    path('buscar-cancion/', views.buscarCancion.as_view(), name='buscar_cancion'),
    path('buscar-suscripcion/', views.buscarSuscripción.as_view(), name='buscar_suscripcion'),
]