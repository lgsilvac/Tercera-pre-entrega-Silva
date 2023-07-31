from django.urls import path, include
from . import views
from .views import * 

app_name = 'miaplicacion'

urlpatterns = [
    path('', index, name="inicio"),
    path('vendedores/', views.vendedores, name='vendedores'),
    path('compradores/', views.compradores, name='compradores'),
    path('productos/', views.productos, name='productos'),
    path('buscar_productos/', views.buscar_productos, name='buscar_productos'),


    path('comprador_form/', compradorForm2, name='comprador_form'),
    path('vendedor_form/', vendedorForm2, name='vendedor_form'),
    path('producto_form/', productoForm2, name='producto_form'),

    path('buscar_producto/', buscar_productos, name='buscar_producto'),

]
