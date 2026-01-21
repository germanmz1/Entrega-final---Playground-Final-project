from django.contrib import admin
from .models import Gasto
from .models import MetodoPago
from .models import Categoria

admin.site.register(Categoria)

admin.site.register(MetodoPago)

admin.site.register(Gasto)