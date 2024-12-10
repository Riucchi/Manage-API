from django.contrib import admin
from .models import Distribuidores, Producto, Distribuidor




admin.site.register(Distribuidor)
admin.site.register(Distribuidores)
admin.site.register(Producto)