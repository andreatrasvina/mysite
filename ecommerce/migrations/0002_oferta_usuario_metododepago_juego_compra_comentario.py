# Generated by Django 4.2.7 on 2023-12-03 03:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadOferta', models.CharField(max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreUsuario', models.CharField(max_length=50, unique=True)),
                ('correoElectronico', models.EmailField(max_length=100, unique=True)),
                ('contrasena', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('apellidoPaterno', models.CharField(max_length=100, null=True)),
                ('apellidoMaterno', models.CharField(max_length=100, null=True)),
                ('fechaNacimiento', models.DateField(null=True)),
                ('genero', models.CharField(choices=[('Mujer', 'Mujer'), ('Hombre', 'Hombre'), ('Prefiero no especificarlo', 'Prefiero no especificarlo')], max_length=30, null=True)),
                ('region', models.CharField(max_length=50, null=True)),
                ('pais', models.CharField(max_length=50, null=True)),
                ('numeroCelular', models.CharField(max_length=15, null=True)),
                ('imagenPerfilURL', models.TextField(null=True)),
                ('biografia', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MetodoDePago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Tarjeta de Crédito', 'Tarjeta de Crédito'), ('Tarjeta de Débito', 'Tarjeta de Débito'), ('PayPal', 'PayPal'), ('Otro', 'Otro')], max_length=20, null=True)),
                ('numero', models.CharField(max_length=20, null=True)),
                ('nombreTitular', models.CharField(max_length=100, null=True)),
                ('fechaVencimiento', models.DateField(null=True)),
                ('codigoSeguridad', models.CharField(max_length=4, null=True)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreJuego', models.CharField(max_length=100)),
                ('descripcion', models.TextField(null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fechaLanzamiento', models.DateField(null=True)),
                ('plataforma', models.CharField(max_length=100, null=True)),
                ('desarrolladora', models.CharField(max_length=100, null=True)),
                ('caracteristicas', models.TextField(null=True)),
                ('imagenURL', models.TextField(null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.categoria')),
                ('oferta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.oferta')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PrecioTotal', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('fechaCompra', models.DateTimeField(auto_now_add=True, null=True)),
                ('juego', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.juego')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('comentario', models.TextField(null=True)),
                ('fechaCalificacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('juego', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.juego')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.usuario')),
            ],
        ),
    ]
