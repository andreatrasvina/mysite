from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.
def get_carrito(request):
    context={}
    template_name = 'ecommerce/carrito.html'
    return render(request, template_name, context)

def get_index(request):
    context={}
    template_name = 'ecommerce/index.html'
    return render(request, template_name, context)


class Categorias(TemplateView):
    template_name = 'ecommerce/categorias.html'
    
class ConfigCuenta(TemplateView):
    template_name = 'ecommerce/config-cuenta.html'
    
class CrearCuenta(TemplateView):
    template_name = 'ecommerce/crear-cuenta.html'
    
class IniciarSesion(TemplateView):
    template_name = 'ecommerce/iniciar-sesion.html'
    
class Juego(TemplateView):
    template_name = 'ecommerce/juego.html'
    
class Ofertas(TemplateView):
    template_name = 'ecommerce/ofertas.html'
    
class Slider(TemplateView):
    template_name = 'ecommerce/slider.html'
    
class Tienda(TemplateView):
    template_name = 'ecommerce/tienda.html'