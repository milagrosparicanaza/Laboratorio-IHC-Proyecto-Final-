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
from django.http import JsonResponse, HttpResponse
from reportlab.pdfgen import canvas
from django.views import View 
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

class ClienteQueryView(View):
    def get(self, request, *args, **kwargs):
      queryset = Cliente.objects.all()
      return JsonResponse(list(queryset.values()), safe = False)

class ReporteClientePDF(View):
  def get(self, request, *args, **kwargs):
    response = HttpResponse(content_type='aplication/pdf')
    response['Content-Disposition'] = 'attachment; filename=ReporteClientes.pdf'
    pdf = canvas.Canvas(response)
    pdf.drawString(100,500,"Hello world.")
    pdf.showPage()
    pdf.save()
    return response
