from django import forms
from .models import Gasto, Categoria, MetodoPago

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre"]

class MetodoPagoForm(forms.ModelForm):
    class Meta:
        model = MetodoPago
        fields = ["nombre"]

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        exclude = ("usuario",)
        labels = {
            "descripcion": "Descripción",
            "monto": "Monto ($)",
            "categoria": "Categoría",
            "metodo_pago": "Método de pago",
            "fecha": "Fecha",
        }