from django.urls import path
from . import views

app_name = "messaging"

urlpatterns = [
    path("", views.bandeja_entrada, name="inbox"),
    path("nuevo/", views.enviar_mensaje, name="enviar"),
    path("<int:pk>/", views.mensaje_detalle, name="detalle"),
]
