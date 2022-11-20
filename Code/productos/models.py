from django.db import models

class Peliculas(models.Model):
    name = models.CharField(max_length=200) #creo una tabla llamada Project
    description = models.TextField()
    director = models.CharField(max_length=200)
    añoSalida = models.DateTimeField()
    categoria = models.CharField(max_length=200)
    
    def __str__(self): #Para que en la applicación no aparezca Project Object sino el nombre
        return self.name

class Musica(models.Model):
    name = models.CharField(max_length=200) #creo una tabla llamada Project
    autor = models.CharField(max_length=200)
    duracion = models.DurationField()
    fecha = models.DateTimeField()
    genero = models.CharField(max_length=200)
    
    def __str__(self): #Para que en la applicación no aparezca Project Object sino el nombre
        return self.name

class Suscripciones(models.Model):
    name = models.CharField(max_length=200) #creo una tabla llamada Project
    description = models.TextField()
    duracion = models.DurationField()
    fecha = models.DateTimeField()
    precio = models.IntegerField()
    
    def __str__(self): #Para que en la applicación no aparezca Project Object sino el nombre
        return self.name