from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import GastoForm, CategoriaForm, MetodoPagoForm


@login_required
def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("crear_categoria")
    else:
        form = CategoriaForm()

    return render(request, "gastos/crear_categoria.html", {"form": form})

@login_required
def crear_metodo_pago(request):
    if request.method == "POST":
        form = MetodoPagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("crear_metodo_pago")
    else:
        form = MetodoPagoForm()

    return render(request, "gastos/crear_metodo_pago.html", {"form": form})

@login_required
def crear_gasto(request):
    if request.method == "POST":
        form = GastoForm(request.POST)
        if form.is_valid():
            gasto = form.save(commit=False)
            gasto.usuario = request.user
            gasto.save()
            return redirect("crear_gasto")
    else:
        form = GastoForm()

    return render(request, "gastos/crear_gasto.html", {"form": form})

