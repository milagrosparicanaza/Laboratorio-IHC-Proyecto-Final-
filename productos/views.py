from django.shortcuts import render
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
class ProductoUpdateView(UpdateView):
  model = Producto
  fields = [
    'nombre',
    'precio',
    'descripcion',
    'foto',
    'vendedor',
  ]
class ProductoDeleteView(DeleteView):
  model = Producto
  success_url = reverse_lazy('productos:productos-list')
