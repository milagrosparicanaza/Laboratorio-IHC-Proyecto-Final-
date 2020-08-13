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

class LisProductos(ListView):
  template_name = 'baseprod.html'
  model = Producto

  def get(self, request, *args, **kwargs):
    name = request.GET['name']
    precio = Producto.objects.get(nombre = name)
    subjects = precio.precio.all()
    data = serializers.serializers('json', subjects, fields=('name','precio','descripcion'))
    return HttpResponse(data, context_type='aplication/json')
