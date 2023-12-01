from django.db import models

# Create your models here.

class Categoria(models.Model):
    nom_categoria=models.CharField(max_length=100)
    
    class Meta:
        db_table='categorias'
