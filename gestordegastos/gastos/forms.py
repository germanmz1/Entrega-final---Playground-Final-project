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
        fields = [
            "titulo",
            "descripcion",
            "monto",
            "categoria",
            "fecha",
            "metodo_pago",
            "codigo"
        ]