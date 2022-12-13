from sqlite3 import IntegrityError
import sqlite3
import unittest
import datetime
import random

from django.test import TestCase
from django.db.utils import IntegrityError
from .models import Escaparates, Peliculas, Musica, Suscripciones, Pedido, ElementoPedido
from django.contrib.auth.models import User
from timeit import default_timer


class peliculasTest(unittest.TestCase):
    print("TEST PELICULAS")

    def test_pelicula_ok(self):
        inicio = default_timer()
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
        fin = default_timer()
        print("test_pelicula_ok: " + str(fin-inicio) + "s")

class musicaTest(unittest.TestCase):
    print("TEST MUSICA")
    def test_cancion_ok(self):
        inicio = default_timer()
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
        fin = default_timer()
        print("test_cancion_ok: " + str(fin-inicio) + "s")

class suscripcionesTest(unittest.TestCase):
    print("TEST SUSCRIPCIONES")
    def test_suscripcion_ok(self):
        inicio = default_timer()
        name = "Suscripcion 1"
        description = "Descripcion de la suscripcion 1"
        duracion = 20000
        precio = 25

        suscripcion1 = Suscripciones(name=name, description=description, duracion=duracion, precio=precio)

        self.assertEqual(suscripcion1.name, name)
        self.assertEqual(suscripcion1.description, description)
        self.assertEqual(suscripcion1.duracion, duracion)
        self.assertEqual(suscripcion1.precio, precio)
        fin = default_timer()
        print("test_suscripcion_ok: " + str(fin-inicio) + "s")

class usuariosTest(unittest.TestCase):
    print("TEST USUARIOS")
    def test_registro_ok(self):
        inicio = default_timer()
        number = str(len(User.objects.all()))
        username="username" + number
        password="password" + number
        first_name="Name" + number
        last_name="Last Name " + number
        email="test" + number + "@sefibox.com"
        
        user = User.objects.create_user(username=username, password=password,first_name=first_name,last_name=last_name,email=email)
        user.save()
        fin = default_timer()
        print("test_registro_ok: " + str(fin-inicio) + "s")

    def test_registro_emptyUsernameKO(self):
        inicio = default_timer()
        number = str(len(User.objects.all()))
        username=""
        password="password" + number
        first_name="Name" + number
        last_name="Last Name " + number
        email="test" + number + "@sefibox.com"
        
        with self.assertRaises(ValueError):
            user = User.objects.create_user(username=username, password=password,first_name=first_name,last_name=last_name,email=email)
            user.save()
        fin = default_timer()
        print("test_registro_emptyUsernameKO: " + str(fin-inicio) + "s")

    def test_registro_existingUsernameKO(self):
        inicio = default_timer()
        number = str(len(User.objects.all()))
        username="username1"
        password="password" + number
        first_name="Name" + number
        last_name="Last Name " + number
        email="test" + number + "@sefibox.com"
        
        with self.assertRaises(IntegrityError):
            user = User.objects.create_user(username=username, password=password,first_name=first_name,last_name=last_name,email=email)
            user.save()
        fin = default_timer()
        print("test_registro_existingUsernameKO: " + str(fin-inicio) + "s")

    def test_busqueda_usuarioOK(self):
        inicio = default_timer()
        id=13
        user1 = User.objects.get(id=int(id))
        self.assertEqual(user1.username, "Prueba990")
        self.assertEqual(user1.first_name, "Prueba0000")
        self.assertEqual(user1.last_name, "Prueba0000")
        self.assertEqual(user1.email, "Prueba0000@gmail.com")
        fin = default_timer()
        print("test_busqueda_usuarioOK: " + str(fin-inicio) + "s")

    def test_busqueda_usuarioNotExistKO(self):
        inicio = default_timer()
        id=99999999
        with self.assertRaises(User.DoesNotExist):
            user1 = User.objects.get(id=int(id))
        fin = default_timer()
        print("test_busqueda_usuarioNotExistKO: " + str(fin-inicio) + "s")

    def test_update_password_usuarioOK(self):
        inicio = default_timer()
        id=13
        user = User.objects.get(id=int(id))

        old_password = user.password
        password = "password" + str(random.randint(0,99))

        while old_password == password:
            password = "password" + str(random.randint(0,99))
        
        user = User.objects.filter(id=id).update(password=password)
        fin = default_timer()
        print("test_update_password_usuarioOK: " + str(fin-inicio) + "s")

class escaparatesTest(unittest.TestCase):
    print("TEST ESCAPARATES")
    def test_escaparate_ok(self):
        inicio = default_timer()
        titulo = "Escaparate 1"
        mostrar = True

        escaparate1 = Escaparates(titulo=titulo, mostrar=mostrar)

        self.assertEqual(escaparate1.titulo, titulo)
        
        self.assertEqual(escaparate1.mostrar, mostrar)
        fin = default_timer()
        print("test_suscripcion_ok: " + str(fin-inicio) + "s")

class pedidoTest(unittest.TestCase):
    print("TEST PEDIDOS")
    def test_pedidos_ok(self):
        inicio = default_timer()
        user = User.objects.get(id=int(1))
        email = "Pedido1@gmail.com"
        nombre = "Pedido 1"
        apellidos = "Pedido 1"
        create_ad = datetime.datetime(2022, 12, 1)
        paid = True
        paid_amount = 300

        pedido1 = Pedido(user=user, email=email, nombre=nombre, apellidos=apellidos, created_ad=create_ad,
         paid=paid, paid_amount=paid_amount)

        self.assertEqual(pedido1.user, user)
        self.assertEqual(pedido1.email, email)
        self.assertEqual(pedido1.nombre, nombre)
        self.assertEqual(pedido1.apellidos, apellidos)
        self.assertEqual(pedido1.created_ad, create_ad)
        self.assertEqual(pedido1.paid, paid)
        self.assertEqual(pedido1.paid_amount, paid_amount)
        fin = default_timer()
        print("test_suscripcion_ok: " + str(fin-inicio) + "s")


class elementoPedidoTest(unittest.TestCase):
    print("TEST ELEMENTO_PEDIDO")
    def test_elemento_pedido_ok(self):
        inicio = default_timer()
        pedido = Pedido.objects.get(id=int(1))
        suscripciones = Suscripciones.objects.get(id=int(1))
        cantidad = 3
        precio = suscripciones.precio * cantidad

        elementoPedido1 = ElementoPedido(pedido=pedido, suscripciones=suscripciones, cantidad=cantidad, precio=precio)

        self.assertEqual(elementoPedido1.pedido, pedido)
        self.assertEqual(elementoPedido1.suscripciones, suscripciones)
        self.assertEqual(elementoPedido1.cantidad, cantidad)
        self.assertEqual(elementoPedido1.precio, precio)
        fin = default_timer()
        print("test_suscripcion_ok: " + str(fin-inicio) + "s")
