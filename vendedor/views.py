from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.utils.decorators import method_decorator
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
  
  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)
    
class VendedorDetailView(DetailView):
  model = Vendedor
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    idus = self.request.user.id
    context['idUsuario'] = idus
    context['idVendedor'] = Vendedor.objects.get(user__id = idus)
    context['productos'] = Producto.objects.filter(vendedor__id = self.kwargs['pk'])
    return context
class VendedorCreateView(CreateView):
  model = Vendedor
  fields = [
    'user',
    'tienda',
  ]
  
  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)
class VendedorUpdateView(UpdateView):
  model = Vendedor
  fields = [
    'user',
    'tienda',
  ]
  
  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)
class VendedorDeleteView(DeleteView):
  model = Vendedor
  success_url = reverse_lazy('vendedor:vendedor-list')
  
  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)
# Create your views here.
