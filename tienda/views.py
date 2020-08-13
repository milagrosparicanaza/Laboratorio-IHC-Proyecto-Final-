from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from productos.models import Producto

class homeView(ListView):
  model = Producto
  template_name = 'index.html'
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['name'] = 'Gustavo'
    return context

