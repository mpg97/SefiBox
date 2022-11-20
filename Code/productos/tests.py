from sqlite3 import IntegrityError
import sqlite3
import unittest
import datetime
import random

from django.test import TestCase
from django.db.utils import IntegrityError
from .models import Peliculas, Musica, Suscripciones
from django.contrib.auth.models import User


class peliculasTest(unittest.TestCase):

    def test_pelicula_ok(self):
        name = "Pelicula 1"
        descripcion = "Esta es una prueba de la Pelicula 1"
        director = "Director 1"
        añoSalida = datetime.datetime(2022, 11, 18)
        categoria = "Categoria 1"

        pelicula1 = Peliculas(name=name, description=descripcion, director=director, añoSalida=añoSalida, categoria=categoria)

        self.assertEqual(pelicula1.name, name)
        self.assertEqual(pelicula1.description, descripcion)
        self.assertEqual(pelicula1.director, director)
        self.assertEqual(pelicula1.añoSalida, añoSalida)
        self.assertEqual(pelicula1.categoria, categoria)

class musicaTest(unittest.TestCase):

    def test_cancion_ok(self):
        name = "Cancion 1"
        autor = "Autor 1"
        duracion = 200
        fecha = datetime.datetime(2022, 11, 18)
        genero = "Genero 1"

        cancion1 = Musica(name=name, autor=autor, duracion=duracion, fecha=fecha, genero=genero)

        self.assertEqual(cancion1.name, name)
        self.assertEqual(cancion1.autor, autor)
        self.assertEqual(cancion1.duracion, duracion)
        self.assertEqual(cancion1.fecha, fecha)
        self.assertEqual(cancion1.genero, genero)

class suscripcionesTest(unittest.TestCase):

    def test_suscripcion_ok(self):
        name = "Suscripcion 1"
        description = "Descripcion de la suscripcion 1"
        duracion = 20000
        fecha = datetime.datetime(2022, 11, 18)
        precio = 25

        suscripcion1 = Suscripciones(name=name, description=description, duracion=duracion, fecha=fecha, precio=precio)

        self.assertEqual(suscripcion1.name, name)
        self.assertEqual(suscripcion1.description, description)
        self.assertEqual(suscripcion1.duracion, duracion)
        self.assertEqual(suscripcion1.fecha, fecha)
        self.assertEqual(suscripcion1.precio, precio)

class usuariosTest(unittest.TestCase):

    def test_registro_ok(self):
        number = str(len(User.objects.all()))
        username="username" + number
        password="password" + number
        first_name="Name" + number
        last_name="Last Name " + number
        email="test" + number + "@sefibox.com"
        
        user = User.objects.create_user(username=username, password=password,first_name=first_name,last_name=last_name,email=email)
        user.save()

    def test_registro_emptyUsernameKO(self):
        number = str(len(User.objects.all()))
        username=""
        password="password" + number
        first_name="Name" + number
        last_name="Last Name " + number
        email="test" + number + "@sefibox.com"
        
        with self.assertRaises(ValueError):
            user = User.objects.create_user(username=username, password=password,first_name=first_name,last_name=last_name,email=email)
            user.save()

    def test_registro_existingUsernameKO(self):
        number = str(len(User.objects.all()))
        username="username1"
        password="password" + number
        first_name="Name" + number
        last_name="Last Name " + number
        email="test" + number + "@sefibox.com"
        
        with self.assertRaises(IntegrityError):
            user = User.objects.create_user(username=username, password=password,first_name=first_name,last_name=last_name,email=email)
            user.save()

    def test_busqueda_usuarioOK(self):
        id=13
        user1 = User.objects.get(id=int(id))
        self.assertEqual(user1.username, "Prueba990")
        self.assertEqual(user1.first_name, "Prueba0000")
        self.assertEqual(user1.last_name, "Prueba0000")
        self.assertEqual(user1.email, "Prueba0000@gmail.com")

    def test_busqueda_usuarioNotExistKO(self):
        id=99999999
        with self.assertRaises(User.DoesNotExist):
            user1 = User.objects.get(id=int(id))

    def test_update_password_usuarioOK(self):
        id=13
        user = User.objects.get(id=int(id))

        old_password = user.password
        password = "password" + str(random.randint(0,99))

        while old_password == password:
            password = "password" + str(random.randint(0,99))
        
        user = User.objects.filter(id=id).update(password=password)
