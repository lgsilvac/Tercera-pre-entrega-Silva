from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Vendedor, Comprador, Producto
from .forms import *
# Create your views here.

def index(request):
    return render(request, "miaplicacion/base.html")

def vendedores(request):
    vendedores = Vendedor.objects.all()
    ctx = {"vendedores": Vendedor.objects.all()}
    return render(request, 'miaplicacion/vendedores.html', {'vendedores': vendedores})

def compradores(request):
    compradores = Comprador.objects.all()
    ctx = {"compradores": Comprador.objects.all()}
    return render(request, 'miaplicacion/compradores.html', {'compradores': compradores})

def productos(request):
    productos = Producto.objects.all()
    ctx = {"productos": Producto.objects.all()}
    return render(request, 'miaplicacion/productos.html', {'productos': productos})

def compradorForm2(request):
    if request.method == "POST":
        miForm = compradorForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            comprador = Comprador(nombre=informacion['nombre'], apellido=informacion['apellido'], correo=informacion['correo'], direccion=informacion['direccion'])
            comprador.save()
            return render(request, "miaplicacion/base.html")
    else:
        miForm = compradorForm()

    return render(request, "miaplicacion/compradorForm.html", {"form":miForm})

def vendedorForm2(request):
    if request.method == "POST":
        miForm = vendedorForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            vendedor = Vendedor(nombre=informacion['nombre'], apellido=informacion['apellido'], correo=informacion['correo'], telefono=informacion['telefono'])
            vendedor.save()
            return render(request, "miaplicacion/base.html")
    else:
        miForm = vendedorForm()

    return render(request, "miaplicacion/vendedorForm.html", {"form":miForm})

def productoForm2(request):
    if request.method == "POST":
        miForm = productoForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            producto = Producto(nombre=informacion['nombre'], precio=informacion['precio'], cantidad=informacion['cantidad'])
            producto.save()
            return render(request, "miaplicacion/base.html")
    else:
        miForm = productoForm()

    return render(request, "miaplicacion/productoForm.html", {"form":miForm})

def buscar_productos(request):
    form = ProductoSearchForm(request.GET)
    resultados = []

    if form.is_valid():
        nombre = form.cleaned_data.get('nombre', None)
        precio_min = form.cleaned_data.get('precio_min', None)
        precio_max = form.cleaned_data.get('precio_max', None)
        cantidad = form.cleaned_data.get('cantidad', None)

        filtro = {}
        if nombre:
            filtro['nombre__icontains'] = nombre
        if precio_min:
            filtro['precio__gte'] = precio_min
        if precio_max:
            filtro['precio__lte'] = precio_max
        if cantidad:
            filtro['cantidad__gte'] = cantidad
        if filtro:
            resultados = Producto.objects.filter(**filtro)

    mensaje = ""

    if not resultados:
        mensaje = "No se encontraron productos con ese nombre."

    return render(request, 'miaplicacion/buscar_productos.html', {'form': form, 'resultados': resultados, 'mensaje': mensaje})