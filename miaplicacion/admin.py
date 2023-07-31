from django.contrib import admin
from .models import Vendedor, Comprador, Producto

# Register your models here.
admin.site.register(Vendedor)
admin.site.register(Comprador)
admin.site.register(Producto)