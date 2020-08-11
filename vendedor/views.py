from django.shortcuts import render
from django.db.models import F
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import (
  ListView,
  DetailView,
  UpdateView,
  DeleteView,
  )
from .models import Vendedor
from productos.models import Producto

class VendedorListView(ListView):
  model = Vendedor
  
class VendedorDetailView(DetailView):
  model = Vendedor
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['productos'] = Producto.objects.filter(vendedor__id = self.kwargs['pk'])
    return context
class VendedorCreateView(CreateView):
  model = Vendedor
  fields = [
    'user',
    'tienda',
  ]
class VendedorUpdateView(UpdateView):
  model = Vendedor
  fields = [
    'user',
    'tienda',
  ]
class VendedorDeleteView(DeleteView):
  model = Vendedor
  success_url = reverse_lazy('vendedor:vendedor-list')
# Create your views here.
