from django.shortcuts import render,redirect, HttpResponse,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

from productos.carrito import Carrito


from .models import Escaparates, Peliculas, Musica, Suscripciones, Pedido,ElementoPedido
from .forms import RegistrationForm,EditUserProfileForm ,PasswordChangeForm, PasswordChangingForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .forms import UserDetailsForm
from django.views import View
import stripe
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView
from .models import Suscripciones
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY
from django.views.generic import ListView
from .context_processor import Carrito,total_carrito
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail
from django.conf import settings

def hello(request):
    escaparates = Escaparates.objects.all()
    print(escaparates)
    return render(request, 'hello.html', {'escaparates' : escaparates})


#Registro de usuarios
def registrar(request):

    if request.method == 'GET':
        return render(request, 'registrar.html', {'form': RegistrationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #Registrando usuario
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'],first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'])
                user.save()
                return HttpResponse('Usuario creado correctamente')
            except:
                return render(request, 'registrar.html', {'form': RegistrationForm, "error": 'El usuario ya existe.'})
        return render(request, 'registrar.html', {'form': RegistrationForm, "error": 'Las contraseñas no coinciden'})

def peliculas(request):
    categorias = categoriaSet()
    peliculas = Peliculas.objects.all()
    return render(request, 'peliculas.html', {'peliculas': peliculas,'categorias' : categorias})

def musica(request):
    generos = generoSet()
    musica = Musica.objects.all()
    return render(request, 'musica.html', {'musica' : musica, 'generos' : generos})

def suscripcion(request):
    suscripcion = Suscripciones.objects.all()
    return render(request, 'suscripciones.html', {'suscripciones' : suscripcion})


#Funciones del carrito
def agregar_suscripcion_carrito(request, suscripcion_id):
    cantidad = request.GET.get('quantity')
    carrito = Carrito(request)
    suscripcion = Suscripciones.objects.get(id=suscripcion_id)
    carrito.agregar(suscripcion, cantidad)
    return redirect("suscripciones")

def eliminar_suscripcion_carrito(request, suscripcion_id):
    carrito = Carrito(request)
    suscripcion = Suscripciones.objects.get(id=suscripcion_id)
    carrito.eliminar(suscripcion)
    return redirect("suscripciones")

def restar_suscripcion_carrito(request, suscripcion_id):
    carrito = Carrito(request)
    suscripcion = Suscripciones.objects.get(id=suscripcion_id)
    carrito.restar(suscripcion)
    return redirect("suscripciones")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("suscripciones")


#Detalles de usuario
def UserDetails1(request):
    user = User.objects.all()
    return render(request,'user_details.html',{'user': user})

def UserDetails(request, id):
    print(id)
    user = User.objects.get(id=int(id))
    return render(request,'user_details2.html',{'user': user})

def PedidoDetails(request, id):
    pedidos = Pedido.objects.filter(id = id)
    items = list()
    for p in pedidos: 
        i = ElementoPedido.objects.filter(pedido = p)
        items.append(i)
    
    return render(request,'pedidos_details.html',{'pedidos': pedidos, 'items': items})


    
#Detalles de usuario
def OneUserDetails(request):
    return render(request,'user_details.html',{'form':UserDetailsForm})

def GetId(request):
    id = request.GET['id']
    if id == '' or id is None:
        return render(request, "user_details_empty.html")
    user = User.objects.filter(id = int(id))
    if user.exists():
        user = user.get(id = int(id))
        pedidos = Pedido.objects.filter(user = user.id)
    else:
        return render(request, "user_details_empty.html")

    return render(request,"user_details2.html",{"user":user, "pedidos": pedidos})

def GetMusicaId(request):
    id = request.GET['id']
    if id == '' or id is None:
        return render(request, "musica_details_empty.html")
    musica = Musica.objects.filter(id = int(id))
    if musica.exists():
        musica = Musica.objects.get(id = int(id))
    else:
        return render(request, "musica_details_empty.html")

    return render(request,"musica_details.html",{"musica":musica})

def GetPeliculaId(request):
    id = request.GET['id']
    if id == '' or id is None:
        return render(request, "pelicula_details_empty.html")
    pelicula = Peliculas.objects.filter(id = int(id))
    if pelicula.exists():
        pelicula = Peliculas.objects.get(id = int(id))
    else:
        return render(request, "pelicula_details_empty.html")

    return render(request,"pelicula_details.html",{"pelicula":pelicula})

#Modificación de usuarios

def UpateUserView(request, id):
    if request.method == 'GET':
        return render(request, "edit_user.html", {'form': EditUserProfileForm})
    else:
        usuario = User.objects.filter(id=id).update(username=request.POST['username'],first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'])
        
        return redirect('')


def UpatePasswordView(request, id):
    if request.method == 'GET':
        return render(request, "change_password.html", {'form':PasswordChangeForm})
    else:
        usuario = User.objects.filter(id=id).update(old_password=request.POST['old_password'],new_password1=request.POST['password1'],new_password2=request.POST['password2'],)
        
        return redirect('user/edit/%s' %id)


# class UpdateUserView(generic.UpdateView):

#     form_class = EditUserProfileForm
#     template_name = "edit_user.html"
#     success_url = reverse_lazy('home')
    
#     def get_object(request,id):
#         return User.objects.get(id=id)



class PasswordChange(PasswordChangeView):
    form_class: PasswordChangingForm(PasswordChangeForm)
    success_url = reverse_lazy('home')


#####################################################################################################################################################
##########################################################################   Pasarela de pago   #####################################################
#####################################################################################################################################################



class SuccessView(TemplateView):
    template_name= 'success.html'

class CancelView(TemplateView):
    template_name= 'cancel.html'


class ProductLandingPageView(TemplateView):
    template_name= "checkout.html"
    
    def get_context_data(self, **kwargs) :
        product = Suscripciones.objects.get(name = "Suscripción de sólo películas")
        context =  super(ProductLandingPageView,self).get_context_data(**kwargs)
        context.update({
            "product":product,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context

class ProductLandingPageView2(TemplateView):
    template_name= "carrito.html"
    
    def get_context_data(self, **kwargs) :
        
        context =  super(ProductLandingPageView,self).get_context_data(**kwargs)
        context.update({
            
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context



class CreateCheckoutSesionView2(View):
    def post(self, request,*args, **kwargs ):
         
            total_carrito1 = total_carrito(request)
            
            self.request = request
            self.session = request.session
            carrito = self.session.get("carrito")
            
            
            items = []
            for item in carrito:
                nombre = carrito[item]['name']
                suscripcion = Suscripciones.objects.get(name= nombre)
                cantidad = carrito[item]['cantidad']
                
                obj = {
                  'price_data':{
                      'currency': 'eur',
                      
                      'product_data': {
                          'name': suscripcion.name
                      },
                      'unit_amount': int(suscripcion.precio*100) ,
                  },
                  'quantity': int(carrito[item]['cantidad'])
                }
                
                
                items.append(obj)
            

            YOUR_DOMAIN= "http://127.0.0.1:8000"
            checkout_session = stripe.checkout.Session.create(
                # customer_email="prueba@gmail.com",
                payment_method_types = ['card'],
                line_items= items, 
                mode='payment',
                success_url=YOUR_DOMAIN + '/',
                cancel_url=YOUR_DOMAIN + '/',
                
            )
            if request.method == 'POST':
                
                nombre = request.POST.get('nombre')
                apellidos=request.POST.get('apellidos')
                email = request.POST.get('email')
                register = request.POST.get('register')
                usuario = User.objects.filter(email=email, first_name = nombre, last_name=apellidos)

                if len(usuario)==0: 
                    usuario = User.objects.get(username = 'invitado')
                else: 
                    usuario = User.objects.get(email=email, first_name = nombre, last_name=apellidos)
                if register == 'on':
                    pedido = Pedido.objects.create(user = usuario,nombre = nombre,apellidos = apellidos,email= email,paid_amount = total_carrito1['total_carrito'])
                else:
                    pedido = Pedido.objects.create(paid_amount = total_carrito1['total_carrito'])
                id = pedido.id
                for item in carrito: 
                    
                    cantidad1 = int(carrito[item]['cantidad'])
                    print(cantidad1)
                    nombre = carrito[item]['name']
                    suscripcion_id = carrito[item]['suscripcion_id']
                    suscripcion1 = Suscripciones.objects.get(id = suscripcion_id)
                    print(type(suscripcion1))
                    precio1 = int(suscripcion1.precio)
                    print(precio1)

                    item = ElementoPedido.objects.create(pedido = pedido, suscripciones = suscripcion1,precio = precio1, cantidad=cantidad1)

                    print(item)
                
                

                # send_mail('The contact form subject', 'This is the message','alvaro.vega.rodriguez@gmail.com',['alvaro.vega.rodriguez@gmail.com'],html_message = html)
                nombre = request.POST.get('nombre')
                total_carrito11=total_carrito1['total_carrito']
                mail = EmailMessage (
                    'Email de compra:',
                    f'Hola {nombre} {apellidos}!!\nEl id del pedido es: {pedido.id}\n\nIMPORTE:{total_carrito11}€',
                    settings.EMAIL_HOST_USER,
                    [email]
                )

                mail.fail_silently = True
                mail.send()

                pedido = Pedido.objects.filter(id=id).update(notified=True)

                #Para vaciar el carro despues de una compra    
                self.session["carrito"] = {}
                self.session.modified = True

                

            
        
            return redirect(checkout_session.url,code = 303)
        
        


class CreateCheckoutSesionView(View):
    def post(self, request,*args, **kwargs ):
        try:
            product_id = self.kwargs["pk"]
            product = Suscripciones.objects.get(id = product_id)
            print(product)
            YOUR_DOMAIN= "http://127.0.0.1:8000"
            checkout_session = stripe.checkout.Session.create(
                payment_method_types = ['card'],
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price_data': {
                            'currency': 'usd',
                            'unit_amount':product.precio,
                            'product_data': {
                                'name': product.name,
                            },
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=YOUR_DOMAIN + '/success',
                cancel_url=YOUR_DOMAIN + '/cancel',
            )
        except Exception as e:
            return str(e)

        return redirect(checkout_session.url,code = 303)


def showcheckout(request): 
    return render(request,'formularioCheckout.html')

######################### EMAIL CONFIRMACIÓN DE COMPRA ###############################

def send_email(email):
    pass


#Busqueda de producto -------------------------------------------

def generoSet():
    lista=[]
    for cancion in Musica.objects.all():
        lista.append(cancion.genero)
    conjunto=set(lista)
    return conjunto

def categoriaSet():
    lista=[]
    for pelicula in Peliculas.objects.all():
        lista.append(pelicula.categoria)
    conjunto=set(lista)
    return conjunto

class buscarPelicula(ListView):
    model = Peliculas
    template_name = 'peliculas.html'
    context_object_name = 'peliculas'

    def get_queryset(self):
        name = self.request.GET.get('q')
        categoria = self.request.GET.get('categoria')
        if categoria in categoriaSet():
            return Peliculas.objects.filter(name__icontains=name).filter(categoria=categoria).order_by('-name')
        else:
            return Peliculas.objects.filter(name__icontains=name).order_by('-name')
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        querySet = self.get_queryset()
        context['categorias'] = categoriaSet()
        context['querySet'] = querySet
        return context

class buscarCancion(ListView):
    model = Musica
    template_name = 'musica.html'
    context_object_name = 'musica'

    def get_queryset(self):
        name = self.request.GET.get('q')
        genero = self.request.GET.get('genero')
        if genero in generoSet():
            return Musica.objects.filter(name__icontains=name).filter(genero=genero).order_by('-name')
        else:
            return Musica.objects.filter(name__icontains=name).order_by('-name')
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        querySet = self.get_queryset()
        context['generos'] = generoSet
        context['querySet'] = querySet
        return context

class buscarSuscripción(ListView):
    model = Suscripciones
    template_name = 'suscripciones.html'
    context_object_name = 'suscripciones'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Suscripciones.objects.filter(name__icontains=query).order_by('-name')

class filtrarCancion(ListView):
    model = Musica
    template_name = 'musica.html'
    context_object_name = 'musica'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Musica.objects.filter(genero__icontains=query).order_by('-name')

class filtrarPelicula(ListView):
    model = Peliculas
    template_name = 'peliculas.html'
    context_object_name = 'peliculas'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Peliculas.objects.filter(categoria__icontains=query).order_by('-name')
    
def buscar_producto(request):
    name = request.GET['q']

    musica = Musica.objects.filter(name__icontains=name).order_by('-name')
    peliculas = Peliculas.objects.filter(name__icontains=name).order_by('-name')
    return render(request, "buscar_producto.html", {'musica':musica, 'peliculas':peliculas, 'page_name':'Search Results'})

# Políticas, servicios y atención -------------------------------

def politica_devoluciones(request):
    return render(request, 'politica_devoluciones.html')

def terminos_servicios(request):
    return render(request, 'terminos_y_servicios.html')

def atencion_cliente(request):
    return render(request, 'atencion_cliente.html')

def politica_privacidad(request):
    return render(request, 'politica_privacidad.html')

def quienes_somos(request):
    return render(request, 'quienes_somos.html')

def politica_envios(request):
    return render(request, 'politica_envio.html')


def GetIdPedido(request):
    id = request.GET['id']
    if id == '' or id is None:
        return render(request,'pedidos_details_empty.html')
    pedido = Pedido.objects.get(id = id)
    user_present = pedido.user != None and pedido.user != ''
    
    items = ElementoPedido.objects.filter(pedido = pedido)
    redeemed = False
    for item in items:
        if redeemed == True:
            break
        else:
            redeemed = item.redeemed
        
    return render(request,'buscador_pedidos2.html',{'pedido': pedido, 'items': items, 'user_present': user_present, 'redeemed': redeemed})

def ActivatePedido(request):
    id = request.GET['id']
    if id == '' or id is None:
        return render(request,'pedidos_details_empty.html')
    pedido = Pedido.objects.get(id = id)
    
    items = ElementoPedido.objects.filter(pedido = pedido)
    for item in items:
        if item.redeemed != True and (item.redemption_date != '' or item.redemption_date != None):
            redemption_date = datetime.now()
            end_date = redemption_date + relativedelta(months=+item.suscripciones.duracion)
            elementoPedido = ElementoPedido.objects.filter(id = item.id).update(redeemed=True, redemption_date = redemption_date, end_date = end_date)
        
    return GetIdPedido(request)


def pedidoDetallesBuscador(request):
    return render(request,'buscador_pedidos.html')
