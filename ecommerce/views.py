from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError

# Create your views here.

def get_carrito(request):
    context={}
    template_name = 'ecommerce/carrito.html'
    return render(request, template_name, context)

def get_categorias(request):
    context={}
    template_name = 'ecommerce/categorias.html'
    return render(request, template_name, context)

def get_configCuenta(request):
    context={}
    template_name = 'ecommerce/config-cuenta.html'
    return render(request, template_name, context)

def get_index(request):
    context={}
    template_name = 'ecommerce/index.html'
    return render(request, template_name, context)

def get_juego(request):
    context={}
    template_name = 'ecommerce/juego.html'
    return render(request, template_name, context)

def get_login(request):
    context={}
    template_name = 'ecommerce/login.html'
    return render(request, template_name, context)

def get_ofertas(request):
    context={}
    template_name = 'ecommerce/ofertas.html'
    return render(request, template_name, context)

def get_slider(request):
    context={}
    template_name = 'ecommerce/slider.html'
    return render(request, template_name, context)

def get_tienda(request):
    context={}
    template_name = 'ecommerce/tienda.html'
    return render(request, template_name, context)

def get_categoria(request):
    context={}
    template_name = 'ecommerce/categoria.html'
    return render(request, template_name, context)

def get_resul(request):
    context={}
    template_name = 'ecommerce/resul.html'
    return render(request, template_name, context)

def get_procesar_pago(request):
    context={}
    template_name = 'ecommerce/procesar-pago.html'
    return render(request, template_name, context)

def get_crearCuenta(request):

    if request.method == 'GET':
        return render(request, 'ecommerce/crear-cuenta.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # se registra al naco
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tienda')
                return HttpResponse('Usuario creado satisfactoriamente')
            except IntegrityError:
                return render(request, 'ecommerce/crear-cuenta.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })

        return render(request, 'ecommerce/crear-cuenta.html', {
            'form': UserCreationForm,
            "error": 'Las contrasenas no coinciden'
        })


def signout(request):
    logout(request)
    return redirect('index')


def get_iniciarSesion(request):
    if request.method == 'GET':
        return render(request, 'ecommerce/iniciar-sesion.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'ecommerce/iniciar-sesion.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contrasena es incorreta'
            })
        else:
            login(request, user)
            return redirect('tienda')
