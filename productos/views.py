from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import (
  ListView,
  DetailView,
  UpdateView,
  DeleteView,
  )
from .models import Producto

class ProductoListView(ListView):
  model = Producto
  
class ProductoDetailView(DetailView):
  model = Producto
class ProductoCreateView(CreateView):
  model = Producto
  fields = [
    'nombre',
    'precio',
    'descripcion',
    'foto',
    'vendedor',
  ]
  
  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)
class ProductoUpdateView(UpdateView):
  model = Producto
  fields = [
    'nombre',
    'precio',
    'descripcion',
    'foto',
    'vendedor',
  ]
  
  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)
class ProductoDeleteView(DeleteView):
  model = Producto
  success_url = reverse_lazy('productos:productos-list')
  
  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)
