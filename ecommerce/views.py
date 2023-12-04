from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/iniciar-sesion/')
def get_carrito(request):
    context={}
    template_name = 'ecommerce/carrito.html'
    return render(request, template_name, context)

def get_categorias(request):
    context={}
    template_name = 'ecommerce/categorias.html'
    return render(request, template_name, context)

@login_required(login_url='/iniciar-sesion/')
def get_configCuenta(request):
    context = {}
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

@login_required(login_url='/iniciar-sesion/')
def get_procesar_pago(request):
    context={}
    template_name = 'ecommerce/procesar-pago.html'
    return render(request, template_name, context)


def get_crearCuenta(request):
    if request.method == 'GET':
        form = UserCreationForm()

        # Elimina los textos predeterminados de los campos
        form.fields['username'].label = ''
        form.fields['password1'].label = ''
        form.fields['password2'].label = ''

        # Elimina los mensajes de ayuda de los campos de contraseña
        form.fields['password1'].help_text = ''
        form.fields['password2'].help_text = ''

        # Elimina el mensaje de ayuda del campo de username
        form.fields['username'].help_text = ''

        # Agrega placeholders a los campos del formulario
        form.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario o correo'
        form.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        form.fields['password2'].widget.attrs['placeholder'] = 'Confirmar contraseña'

        return render(request, 'ecommerce/crear-cuenta.html', {'form': form})
    else:
        if request.POST['password1'] == request.POST['password2']:
            # se registra al usuario
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
            "error": 'Las contraseñas no coinciden'
        })



# def get_crearCuenta(request):
#     if request.method == 'GET':
#         return render(request, 'ecommerce/crear-cuenta.html', {
#             'form': UserCreationForm
#         })
#     else:
#         if request.POST['password1'] == request.POST['password2']:
#             # se registra al naco
#             try:
#                 user = User.objects.create_user(
#                     username=request.POST['username'], password=request.POST['password1'])
#                 user.save()
#                 login(request, user)
#                 return redirect('tienda')
#                 return HttpResponse('Usuario creado satisfactoriamente')
#             except IntegrityError:
#                 return render(request, 'ecommerce/crear-cuenta.html', {
#                     'form': UserCreationForm,
#                     "error": 'El usuario ya existe'
#                 })

#         return render(request, 'ecommerce/crear-cuenta.html', {
#             'form': UserCreationForm,
#             "error": 'Las contrasenas no coinciden'
#         })


def signout(request):
    logout(request)
    return redirect('index')


# def get_iniciarSesion(request):
#     if request.method == 'GET':
#         return render(request, 'ecommerce/iniciar-sesion.html', {
#             'form': AuthenticationForm
#         })
#     else:
#         user = authenticate(
#             request, username=request.POST['username'], password=request.POST['password'])

#         if user is None:
#             return render(request, 'ecommerce/iniciar-sesion.html', {
#                 'form': AuthenticationForm,
#                 'error': 'Usuario o contrasena es incorreta'
#             })
#         else:
#             login(request, user)
#             return redirect('tienda')

from django.contrib.auth.forms import AuthenticationForm

def get_iniciarSesion(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        # Elimina los textos predeterminados de los campos
        form.fields['username'].label = ''
        form.fields['password'].label = ''
        # Agrega placeholders a los campos del formulario
        form.fields['username'].widget.attrs['placeholder'] = 'Dirección de correo electrónico'
        form.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
        return render(request, 'ecommerce/iniciar-sesion.html', {'form': form})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            form = AuthenticationForm()
            # Elimina los textos predeterminados de los campos
            form.fields['username'].label = ''
            form.fields['password'].label = ''
            # Agrega placeholders a los campos del formulario
            form.fields['username'].widget.attrs['placeholder'] = 'Usuario'
            form.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
            return render(request, 'ecommerce/iniciar-sesion.html', {
                'form': form,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('tienda')


