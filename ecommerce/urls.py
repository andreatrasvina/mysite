from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    
    path('index/', views.get_index, name='index'),
    path('carrito/', views.get_carrito, name='carrito'),
    path('categorias/', views.get_categorias, name='categorias'),
    path('config-cuenta/', views.get_configCuenta, name='config-cuenta'),
    path('crear-cuenta/', views.get_crearCuenta, name='crear-cuenta'),
    path('iniciar-sesion/', views.get_iniciarSesion, name='iniciar-sesion'),
    path('juego/', views.get_juego, name='juego'),
    path('login/', views.get_login, name='login'),
    path('ofertas/', views.get_ofertas, name='ofertas'),
    path('slider/', views.get_slider, name='slider'),
    path('tienda/', views.get_tienda, name='tienda'),
    path('categoria/', views.get_categoria, name='categoria'),
    
]