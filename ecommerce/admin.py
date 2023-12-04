from django.contrib import admin

# Register your models here.
from .models import Categoria
from .models import Usuario
from .models import Oferta
from .models import Juego
from .models import Comentario
from .models import Compra
from .models import MetodoDePago

from .models import JuegosPublicados
admin.site.register(JuegosPublicados)

from .models import slidersPromocionales
admin.site.register(slidersPromocionales)

admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(Oferta)
admin.site.register(Juego)
admin.site.register(Comentario)
admin.site.register(Compra)
admin.site.register(MetodoDePago)