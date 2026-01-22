from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Gasto
from django.contrib import messages
from django.views.generic import DetailView
from .forms import GastoForm, CategoriaForm, MetodoPagoForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

from django.contrib import messages

class GastoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Gasto
    form_class = GastoForm
    template_name = "gastos/gasto_update.html"
    success_url = reverse_lazy('gastos:lista')

    def form_valid(self, form):
        messages.success(self.request, "Gasto actualizado correctamente")
        return super().form_valid(form)

    def test_func(self):
        gasto = self.get_object()
        return gasto.usuario == self.request.user

class GastoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Gasto
    template_name = "gastos/gasto_delete.html"
    success_url = reverse_lazy('gastos:lista')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Gasto eliminado 🗑️")
        return super().delete(request, *args, **kwargs)

    def test_func(self):
        gasto = self.get_object()
        return gasto.usuario == self.request.user

    def get_success_url(self):
        return reverse_lazy('gastos:lista')

class GastoDetailView(DetailView):
    model = Gasto
    template_name = "gastos/gasto_detail.html"
    context_object_name = "gasto"

class GastoListView(LoginRequiredMixin, ListView):
    model = Gasto
    template_name = "gastos/gasto_list.html"
    context_object_name = "gastos"

    def get_queryset(self):
        return Gasto.objects.filter(usuario=self.request.user)

@login_required
def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("gastos:crear_categoria")
    else:
        form = CategoriaForm()

    return render(request, "gastos/crear_categoria.html", {"form": form})

@login_required
def crear_metodo_pago(request):
    if request.method == "POST":
        form = MetodoPagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("gastos:crear_metodo_pago")
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
            messages.success(request, "Gasto creado correctamente")
            return redirect("gastos:lista")
    else:
        form = GastoForm()

    return render(request, "gastos/crear_gasto.html", {"form": form})
