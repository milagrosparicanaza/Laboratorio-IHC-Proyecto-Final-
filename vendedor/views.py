from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
from django.views import View
from django.http import JsonResponse
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
    try:
      context['vend'] = Vendedor.objects.get(user__id = user).id
    except:
      context['vend'] = None
    context['productos'] = Producto.objects.filter(vendedor__id = self.kwargs['pk'])
    return context
    
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
    
class VendedorQueryView(View):
  def get(self, request, *args, **kwargs):
      queryset = Vendedor.objects.all()
      return JsonResponse(list(queryset.values()), safe = False)
# Create your views here.
