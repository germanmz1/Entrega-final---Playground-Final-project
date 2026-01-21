from django.urls import path
from . import views

app_name = "gastos"

urlpatterns = [
    path("crear/", views.crear_gasto, name="crear_gasto"),
    path("categoria/crear/", views.crear_categoria, name="crear_categoria"),
    path("metodo-pago/crear/", views.crear_metodo_pago, name="crear_metodo_pago"),
]