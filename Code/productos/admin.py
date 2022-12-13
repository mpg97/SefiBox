from django.contrib import admin
from .models import Escaparates, Peliculas, Musica, Suscripciones,Pedido,ElementoPedido


admin.site.register(Peliculas)
admin.site.register(Musica)
admin.site.register(Suscripciones)
admin.site.register(Escaparates)
admin.site.register(Pedido)
admin.site.register(ElementoPedido)