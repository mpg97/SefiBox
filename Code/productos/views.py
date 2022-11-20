from django.shortcuts import render,redirect, HttpResponse,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Peliculas, Musica, Suscripciones
from .forms import RegistrationForm,EditUserProfileForm ,PasswordChangeForm, PasswordChangingForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .forms import UserDetailsForm
from django.views.generic import ListView

def hello(request):
    return render(request, 'hello.html')

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
    peliculas = Peliculas.objects.all()
    return render(request, 'peliculas.html', {'peliculas' : peliculas})

def musica(request):
    musica = Musica.objects.all()
    return render(request, 'musica.html', {'musica' : musica})

def suscripcion(request):
    suscripcion = Suscripciones.objects.all()
    return render(request, 'suscripciones.html', {'suscripciones' : suscripcion})
    

#Detalles de usuario
def UserDetails1(request):
    user = User.objects.all()
    return render(request,'user_details.html',{'user': user})

def UserDetails(request, id):
    print(id)
    user = User.objects.get(id=int(id))
    return render(request,'user_details2.html',{'user': user})

    
#Detalles de usuario
def OneUserDetails(request):
    return render(request,'user_details.html',{'form':UserDetailsForm})

def GetId(request):
    id = request.GET['id']
    user = get_object_or_404(User, id=int(id))
    return render(request,"user_details2.html",{"user":user})

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

    

#Busqueda de producto -------------------------------------------

class buscarPelicula(ListView):
    model = Peliculas
    template_name = 'peliculas.html'
    context_object_name = 'peliculas'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Peliculas.objects.filter(name__icontains=query).order_by('-name')

class buscarCancion(ListView):
    model = Musica
    template_name = 'musica.html'
    context_object_name = 'musica'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Musica.objects.filter(name__icontains=query).order_by('-name')

class buscarSuscripción(ListView):
    model = Suscripciones
    template_name = 'suscripciones.html'
    context_object_name = 'suscripciones'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Suscripciones.objects.filter(name__icontains=query).order_by('-name')