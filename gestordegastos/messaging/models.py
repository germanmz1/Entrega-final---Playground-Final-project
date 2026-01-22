from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes_enviados")
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes_recibidos")
    asunto = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.asunto} - {self.remitente}"