from django import forms

class compradorForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido", max_length=50, required=True)
    correo = forms.EmailField(label="Correo", max_length=50, required=True)
    direccion = forms.CharField(label="Direccion", max_length=50, required=True)

class vendedorForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido", max_length=50, required=True)
    correo = forms.CharField(label="Correo", max_length=50, required=True)
    telefono = forms.CharField(label="Direccion", max_length=50, required=True)

class productoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    precio = forms.IntegerField(label="Precio CLP", required=True)
    cantidad = forms.IntegerField(label="Cantidad", required=True)

class ProductoSearchForm(forms.Form):
    nombre = forms.CharField(required=False, label="Nombre del producto")