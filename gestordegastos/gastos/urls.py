from django.urls import path
from . import views
from .views import GastoListView
from .views import GastoDetailView
from .views import GastoUpdateView
from .views import GastoDeleteView
app_name = "gastos"

urlpatterns = [
        path("", GastoListView.as_view(), name="lista"),
    path("crear/", views.crear_gasto, name="crear_gasto"),
    path("categoria/crear/", views.crear_categoria, name="crear_categoria"),
    path("metodo-pago/crear/", views.crear_metodo_pago, name="crear_metodo_pago"),
    path("<int:pk>/", GastoDetailView.as_view(), name="detalle_gasto"),
    path("<int:pk>/editar/", GastoUpdateView.as_view(), name="editar_gasto"),
    path("<int:pk>/borrar/", GastoDeleteView.as_view(), name="borrar_gasto"),
]