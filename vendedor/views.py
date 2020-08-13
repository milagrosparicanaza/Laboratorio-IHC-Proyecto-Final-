from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
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
    user = self.request.user.id
    context['thisVend'] = self.object.id
    context['vend'] = Vendedor.objects.get(user__id = user).id
    context['productos'] = Producto.objects.filter(vendedor__id = self.kwargs['pk'])
    return context
  #@method_decorator(user_passes_test(property_check))
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)
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
