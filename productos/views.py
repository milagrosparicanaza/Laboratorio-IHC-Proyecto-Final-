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
from vendedor.models import Vendedor

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
  
  def get_success_url(self, **kwargs):
    user = self.request.user.id
    idvend = Vendedor.objects.get(user__id = user).id
    return f'/vendedores/{idvend}'
    
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
  success_url = '/vendedores'
  def get_success_url(self, **kwargs):
    user = self.request.user.id
    idvend = Vendedor.objects.get(user__id = user).id
    return f'/vendedores/{idvend}'
  
  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)
