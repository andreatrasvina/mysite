from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from . import views

# urls.py
from django.urls import path
from .views import juego, agregar_al_carrito, carrito

from django.urls import path
from .views import juego

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
    path('resul/', views.get_resul, name='resul'),
    path('procesar-pago/', views.get_procesar_pago, name='procesar-pago'),
    path('logout/', views.signout, name='logout'),
    path('lista_juegos', views.lista_juegos, name='lista_juegos'),
    path('juego/<int:juego_id>/', views.detalle_juego, name='detalle_juego'),
    path('buscar/', views.buscar_productos, name='buscar_productos'),
    path('historial/', views.get_historial, name='historial'),
    path('eliminar_del_carrito/<int:compra_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),

    path('juego/<int:juego_id>/', juego, name='juego'),
    path('agregar_al_carrito/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', carrito, name='carrito'),    
]