from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nom_categoria=models.CharField(max_length=100)
    
    class Meta:
        db_table='categorias'
        
class JuegosPublicados(models.Model):
    nombreJuego = models.CharField(max_length=100, null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    clasificacion = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    titulodescripcion = models.TextField(null=True)
    descripcion = models.TextField(null=True)
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    
    class Meta:
        db_table='juegosPublicados'
        
        
class ComprasRegistradas(models.Model):
    juego = models.ForeignKey(JuegosPublicados, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    cantidad = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'comprasRegistradas'
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

# Modelo para Usuarios
class Usuario(models.Model):
    nombreUsuario = models.CharField(max_length=50, unique=True, null=False)
    correoElectronico = models.EmailField(max_length=100, unique=True, null=False)
    contrasena = models.CharField(max_length=100, null=False)
    is_active = models.BooleanField(default=True, null=False)
    nombre = models.CharField(max_length=100, null=True)
    apellidoPaterno = models.CharField(max_length=100, null=True)
    apellidoMaterno = models.CharField(max_length=100, null=True)
    fechaNacimiento = models.DateField(null=True)
    GENERO_CHOICES = [
        ('Mujer', 'Mujer'),
        ('Hombre', 'Hombre'),
        ('Prefiero no especificarlo', 'Prefiero no especificarlo'),
    ]
    genero = models.CharField(max_length=30, choices=GENERO_CHOICES, null=True)
    region = models.CharField(max_length=50, null=True)
    pais = models.CharField(max_length=50, null=True)
    numeroCelular = models.CharField(max_length=15, null=True)
    imagenPerfilURL = models.TextField(null=True)
    biografia = models.TextField(null=True)

# Modelo para Ofertas
class Oferta(models.Model):
    cantidadOferta = models.CharField(max_length=5, null=True)
    
# Modelo para Juegos
class Juego(models.Model):
    nombreJuego = models.CharField(max_length=100, null=False)
    descripcion = models.TextField(null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    fechaLanzamiento = models.DateField(null=True)
    plataforma = models.CharField(max_length=100, null=True)
    desarrolladora = models.CharField(max_length=100, null=True)
    caracteristicas = models.TextField(null=True)
    imagenURL = models.TextField(null=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, null=False)
    oferta = models.ForeignKey('Oferta', on_delete=models.CASCADE, null=False)

# Modelo para Comentarios
class Comentario(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=True)
    juego = models.ForeignKey('Juego', on_delete=models.CASCADE, null=True)
    calificacion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    comentario = models.TextField(null=True)
    fechaCalificacion = models.DateTimeField(auto_now_add=True, null=True)

# Modelo para Compras
class Compra(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=True)
    juego = models.ForeignKey('Juego', on_delete=models.CASCADE, null=True)
    PrecioTotal = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    fechaCompra = models.DateTimeField(auto_now_add=True, null=True)

# Modelo para Métodos de Pago
class MetodoDePago(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=True)
    TIPO_CHOICES = [
        ('Tarjeta de Crédito', 'Tarjeta de Crédito'),
        ('Tarjeta de Débito', 'Tarjeta de Débito'),
        ('PayPal', 'PayPal'),
        ('Otro', 'Otro'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, null=True)
    numero = models.CharField(max_length=20, null=True)
    nombreTitular = models.CharField(max_length=100, null=True)
    fechaVencimiento = models.DateField(null=True)
    codigoSeguridad = models.CharField(max_length=4, null=True)