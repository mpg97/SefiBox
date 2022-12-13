from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PasswordChangeView
from .views import CreateCheckoutSesionView,ProductLandingPageView,CancelView,SuccessView, CreateCheckoutSesionView2,ProductLandingPageView2
from django.conf import settings
from django.conf.urls.static import static

from .views import PasswordChangeView, agregar_suscripcion_carrito, eliminar_suscripcion_carrito, limpiar_carrito, restar_suscripcion_carrito

urlpatterns = [
    path('', views.hello, name=''),
    path('registrar/', views.registrar, name='registrar'), #el name=registrar se hace por si se quiere cambiar el nombre del path no habrá que cambiar todo el proyecto.
    path('peliculas/', views.peliculas, name='peliculas'),
    path('peliculas/details/',views.GetPeliculaId,name='peliculadetails'),
    path('musica/', views.musica, name='musica'),
    path('musica/details/',views.GetMusicaId,name='musicadetails'),
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

    ####################### Pasarela de pago ###################################
    path('create-checkout-session/', CreateCheckoutSesionView2.as_view(),name='createcheckoutsession2'),
    path('landing',ProductLandingPageView.as_view(),name='landingview'),
    path('cancel',CancelView.as_view(),name= 'cancelview'),
    path('success',SuccessView.as_view(),name= 'successview'),
    path('create-checkout-session/<pk>', CreateCheckoutSesionView.as_view(),name='createcheckoutsession'),

    #Busqueda producto ------------------------------
    path('buscar-pelicula/', views.buscarPelicula.as_view(), name='buscar_pelicula'),
    path('filtrar-pelicula/', views.filtrarPelicula.as_view(), name='filtrar_pelicula'),
    path('buscar-cancion/', views.buscarCancion.as_view(), name='buscar_cancion'),
    path('filtrar-cancion/', views.filtrarCancion.as_view(), name='filtrar_cancion'),
    path('buscar-suscripcion/', views.buscarSuscripción.as_view(), name='buscar_suscripcion'),
    path('buscar-pedido/', views.pedidoDetallesBuscador, name='buscar_pedido'),
    path('buscar-pedido/sent', views.GetIdPedido, ),
    path('buscar-pedido/activate/sent', views.ActivatePedido, name='activate_pedido'),
    path('check',views.showcheckout),
    path('buscar-producto/', views.buscar_producto, name='buscar_producto'),

    #Urls Carrito -----------------------------------
    path('agregar/<int:suscripcion_id>/', agregar_suscripcion_carrito, name="Add"),
    path('eliminar/<int:suscripcion_id>/', eliminar_suscripcion_carrito, name="Del"),
    path('restar/<int:suscripcion_id>/', restar_suscripcion_carrito, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),

    #Detalles de pedido --------------------------------
    path('user/sent/pedido/detalles/<int:id>',views.PedidoDetails, name='detalles_pedido'),
    
    #Políticas, about, etc. ----------------------------    
    path('devoluciones/', views.politica_devoluciones, name='devolucones'),
    path('terminos/', views.terminos_servicios, name='terminos'),
    path('atencion/', views.atencion_cliente, name='atencion'),
    path('politica-privacidad/', views.politica_privacidad, name='privacidad'),
    path('quienes-somos/', views.quienes_somos, name='quienes_somos'),
    path('envios/', views.politica_envios, name='envios'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)