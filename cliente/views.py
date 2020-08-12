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
from .models import Cliente

class ClienteListView(ListView):
  model = Cliente
  
class ClienteDetailView(DetailView):
  model = Cliente

class ClienteCreateView(CreateView):
  model = Cliente
  fields = [
    'user',
    'credit_card',
  ]
class ClienteUpdateView(UpdateView):
  model = Cliente
  fields = [
    'user',
    'credit_card',
  ]
class ClienteDeleteView(DeleteView):
  model = Cliente
  success_url = reverse_lazy('cliente:cliente-list')