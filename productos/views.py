from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django import forms
from django.views.generic.edit import CreateView
from django.views.generic import (
  ListView,
  DetailView,
  UpdateView,
  DeleteView,
  )
from django.views import View
from django.http import JsonResponse
from .models import Producto
from vendedor.models import Vendedor

class ProductoListView(ListView):
  model = Producto
  
class ProductoDetailView(DetailView):
  model = Producto
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user = self.request.user.id
    if user != None:
    	context['Vendedor'] = Vendedor.objects.get(user__id = user)
    return context
  
class ProductoForm(forms.ModelForm):
  class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'foto', 'vendedor']
        widgets = {
          'nombre': forms.TextInput(
            attrs={
              'class': 'form-control',
            }
          ),
          'precio': forms.NumberInput(
            attrs={
              'class': 'form-control',
            }
          ),
          'descripcion': forms.Textarea(
            attrs={
              'class': 'form-control',
              'rows': '4',
            }
          ),
          'foto': forms.FileInput(
            attrs={
              'class': 'custom-file-input',
            }
          ),
          'vendedor': forms.Select(
            attrs={
              'class': 'custom-select',
            }
          )
        }

class ProductoCreateView(CreateView):
  form_class = ProductoForm
  model = Producto

  def get_success_url(self, **kwargs):
    user = self.request.user.id
    idvend = Vendedor.objects.get(user__id = user).id
    return f'/vendedores/{idvend}'
    
  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)
    
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user = self.request.user.id
    titulo = 'Nuevo Producto'
    context['titulo'] = titulo
    if user != None:
    	context['Vendedor'] = Vendedor.objects.get(user__id = user)
    return context
    
class ProductoUpdateView(UpdateView):
  form_class = ProductoForm
  model = Producto
  
  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)
    
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user = self.request.user.id
    titulo = 'Editar Producto'
    context['titulo'] = titulo
    if user != None:
    	context['Vendedor'] = Vendedor.objects.get(user__id = user)
    return context
    
class ProductoDeleteView(DeleteView):
  model = Producto
  
  def get_success_url(self, **kwargs):
    user = self.request.user.id
    idvend = Vendedor.objects.get(user__id = user).id
    return f'/vendedores/{idvend}'

  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)
    
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user = self.request.user.id
    if user != None:
    	context['Vendedor'] = Vendedor.objects.get(user__id = user)
    return context
    
class ProductoQueryView(View):
  def get(self, request, *args, **kwargs):
      queryset = Producto.objects.all()
      return JsonResponse(list(queryset.values()), safe = False)
