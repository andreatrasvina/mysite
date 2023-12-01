from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    
    path('', views.get_index, name='index'),
    path('carrito/', views.get_carrito, name='carrito'),
    
    
]