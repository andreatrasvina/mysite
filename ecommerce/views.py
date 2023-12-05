from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required



#MODELOS IMPORTADOS
from .models import JuegosPublicados, ComprasRegistradas, slidersPromocionales

# Create your views here.
def lista_juegos(request):
    juegos = JuegosPublicados.objects.all()
    context = {'juegos': juegos}
    return render(request, 'ecommerce/lista_juegos.html', context)

from django.shortcuts import render, get_object_or_404
from .models import JuegosPublicados, ComprasRegistradas

from django.shortcuts import render, get_object_or_404
from .models import JuegosPublicados
from django.db.models import Sum

@login_required
def detalle_juego(request, juego_id):
    juego = get_object_or_404(JuegosPublicados, pk=juego_id)

    if request.method == 'POST':
        # Procesar la compra y agregar al carrito
        cantidad = int(request.POST.get('cantidad', 1))
        user = request.user
        precio_total = juego.precio * cantidad
        ComprasRegistradas.objects.create(juego=juego, user=user, cantidad=cantidad, total=precio_total)

        return redirect('carrito')

    # Obtener todas las compras en el carrito para el usuario actual
    carrito = ComprasRegistradas.objects.filter(user=request.user)

    # Calcular la suma de los precios de los juegos en el carrito
    total_precio_carrito = carrito.aggregate(Sum('juego__precio'))['juego__precio__sum']

    return render(request, 'ecommerce/juego.html', {'juego': juego, 'carrito': carrito, 'total_precio_carrito': total_precio_carrito})

    
# AQUI 



def buscar_productos(request):
    if request.method == 'POST':
        query = request.POST.get('q', '')  # Obtén el texto de búsqueda del formulario POST

        # Lógica para manejar la búsqueda basada en POST
        resultados = JuegosPublicados.objects.filter(nombreJuego__icontains=query)


        context = {'resultados': resultados, 'query': query}
        return render(request, 'ecommerce/resul.html', context)

    # Si llega una solicitud GET o cualquier otra, redirige a la vista de búsqueda
    return redirect('buscar_productos')


@login_required(login_url='/iniciar-sesion/')
def get_carrito(request):
    
    carrito = ComprasRegistradas.objects.filter(user=request.user)
    print(carrito)
    return render(request, 'ecommerce/carrito.html', {'carrito': carrito})


def get_categorias(request):
    juegos = JuegosPublicados.objects.all()
    context = {'juegos': juegos}
    return render(request, 'ecommerce/categorias.html', context)

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

def get_historial(request):
    context={}
    template_name = 'ecommerce/historial.html'
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


def signout(request):
    logout(request)
    return redirect('index')


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


def get_tienda(request):
    sliders = slidersPromocionales.objects.all()
    context = {'sliders': sliders}
    return render(request, 'ecommerce/tienda.html', context)


# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import JuegosPublicados, ComprasRegistradas

def agregar_al_carrito(request):
    if request.method == 'POST':
        juego_id = request.POST.get('juego_id')
        juego = JuegosPublicados.objects.get(id=juego_id)
        user = request.user
        print(juego_id)
        # Verifica si el juego ya está en el carrito del usuario
        compra_existente = ComprasRegistradas.objects.filter(juego=juego, user=user).exists()

        if not compra_existente:
            # Crea una nueva compra en el carrito
            ComprasRegistradas.objects.create(juego=juego, user=user)
            messages.success(request, f'{juego.nombreJuego} se ha añadido al carrito.')
        else:
            messages.info(request, f'{juego.nombreJuego} ya está en tu carrito.')

        return redirect('carrito')
    else:
        # Manejar otro caso si es necesario
        pass


# views.py
from django.shortcuts import render
from .models import ComprasRegistradas

def carrito(request):
    print("hola")
    if request.user.is_authenticated:
        # Obtén las compras del usuario autenticado
        compras = ComprasRegistradas.objects.filter(user=request.user)
        
        return render(request, 'carrito.html', {'compras': compras})
    else:
        # Manejar el caso si el usuario no está autenticado
        # Puedes redirigirlo a la página de inicio de sesión, por ejemplo
        return render(request, 'carrito.html')  # Ajusta esto según tus necesidades



from django.shortcuts import render, get_object_or_404
from .models import JuegosPublicados

def juego(request, juego_id):
    juego = JuegosPublicados.objects.get(id=juego_id)# Obtén el juego desde la base de datos
    return render(request, 'ecommerce/juego.html', {'juego': juego})


def eliminar_del_carrito(request, compra_id):
    compra = get_object_or_404(ComprasRegistradas, id=compra_id)

    # Verifica si la compra pertenece al usuario actual antes de eliminarla
    if compra.user == request.user:
        compra.delete()

    return redirect('carrito')

# def detalle_juego(request, juego_id):
#     juego = JuegosPublicados.objects.get(pk=juego_id)# Obtén el juego desde la base de datos
#     return render(request, 'ecommerce/juego.html', {'juego': juego})