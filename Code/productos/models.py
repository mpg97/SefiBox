from django.db import models
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User

class Peliculas(models.Model):
    name = models.CharField(max_length=200) #creo una tabla llamada Project
    description = models.TextField()
    director = models.CharField(max_length=200)
    añoSalida = models.DateTimeField()
    duration = models.DurationField()
    categoria = models.CharField(max_length=200)
    imagen = ImageField(upload_to="static/", default="anything")
    def __str__(self): #Para que en la applicación no aparezca Project Object sino el nombre
        return self.name

class Musica(models.Model):
    name = models.CharField(max_length=200) #creo una tabla llamada Project
    autor = models.CharField(max_length=200)
    duracion = models.DurationField()
    fecha = models.DateTimeField()
    genero = models.CharField(max_length=200)
    imagen = ImageField(upload_to="static/")

    def __str__(self): #Para que en la applicación no aparezca Project Object sino el nombre
        return self.name

class Suscripciones(models.Model):
    name = models.CharField(max_length=200) #creo una tabla llamada Project
    description = models.TextField()
    duracion = models.FloatField(default=1.0) #Duración en meses
    precio = models.IntegerField()
    peliculas = models.ManyToManyField(Peliculas, blank=True)
    canciones = models.ManyToManyField(Musica, blank=True)
    
    def __str__(self): #Para que en la applicación no aparezca Project Object sino el nombre
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.precio)

class Escaparates(models.Model):
    titulo = models.CharField(max_length=30)
    peliculas = models.ManyToManyField(Peliculas, blank=True)
    canciones = models.ManyToManyField(Musica, blank=True)
    suscripciones = models.ManyToManyField(Suscripciones, blank=True)
    mostrar = models.BooleanField(default=False)

    #Se encarga de que si un escaparate pasa a mostrarse, el que esté activo, se oculta
    def save(self, *args, **kwargs):
        if self.mostrar:
            try:
                temp = Escaparates.objects.get(mostrar=True)
                if self != temp:
                    temp.mostrar = False
                    temp.save()
            except Escaparates.DoesNotExist:
                pass
        super(Escaparates, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo


class Pedido (models.Model): 
    user = models.ForeignKey(User, related_name="orders", blank=True, null=True, on_delete=models.CASCADE)
    email = models.CharField(max_length=255,null=True,default=False)
    nombre = models.CharField(max_length=100,null=True,default=False)
    apellidos = models.CharField(max_length=200,null=True,default=False)
    created_ad = models.DateTimeField(auto_now_add=True)
    notified = models.BooleanField(default=False) #Notificado
    paid = models.BooleanField(default= False)
    paid_amount = models.IntegerField(blank=True, null=True)


class ElementoPedido (models.Model):
    pedido = models.ForeignKey(Pedido, related_name='items', on_delete=models.CASCADE)
    suscripciones = models.ForeignKey(Suscripciones, related_name='suscripciones', on_delete=models.CASCADE)
    precio = models.IntegerField(default= False)
    cantidad = models.IntegerField(default= False)
    redeemed = models.BooleanField(default=False) #Canjeado
    redemption_date = models.DateTimeField(null=True) #Fecha canjeo
    end_date = models.DateTimeField(null=True)
