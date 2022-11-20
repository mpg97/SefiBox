from django.contrib import admin
from .models import Peliculas, Musica, Suscripciones


admin.site.register(Peliculas)
admin.site.register(Musica)
admin.site.register(Suscripciones)