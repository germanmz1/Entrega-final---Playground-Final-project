from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm


@login_required
def bandeja_entrada(request):
    mensajes = Message.objects.filter(destinatario=request.user).order_by("-fecha")
    return render(request, "messaging/inbox.html", {"mensajes": mensajes})


@login_required
def mensaje_detalle(request, pk):
    mensaje = get_object_or_404(
        Message,
        pk=pk,
        destinatario=request.user
    )
    return render(request, "messaging/detail.html", {"mensaje": mensaje})


@login_required
def enviar_mensaje(request):
    if request.method == "POST":
        form = MessageForm(request.POST, user=request.user)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            return redirect("messaging:inbox")
    else:
        form = MessageForm(user=request.user)

    return render(request, "messaging/enviar.html", {"form": form})
