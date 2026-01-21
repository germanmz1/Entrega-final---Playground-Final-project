from django.db import models
from django.contrib.auth.models import User


class Gasto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)
    fecha = models.DateField()
    metodo_pago = models.CharField(max_length=50)
    codigo = models.IntegerField(unique=True)

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - ${self.monto}"