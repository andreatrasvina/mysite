from django.urls import path

from . import views

urlpatterns =[
    path('login/', views.login_form, name='login_user')
]