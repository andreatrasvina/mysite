from django.shortcuts import render

from django.views.generic import TemplateView

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

def get_crearCuenta(request):
    context={}
    template_name = 'ecommerce/crear-cuenta.html'
    return render(request, template_name, context)

def get_index(request):
    context={}
    template_name = 'ecommerce/index.html'
    return render(request, template_name, context)

def get_iniciarSesion(request):
    context={}
    template_name = 'ecommerce/iniciar-sesion.html'
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