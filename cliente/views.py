#from django.conf import settings
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
#from django.template.loarder import get_template
from django.core.mail import EmailMultiAlternatives

class ClienteListView(ListView):
  model = Cliente
  
class ClienteDetailView(DetailView):
  model = Cliente

class ClienteCreateView(CreateView):
  model = Cliente
  templates_name = 'base.html'
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

def index(request):
  if request.method == 'POST':
    mail = request.POST.get('mail')

    send_email(mail)
  return render(request, 'vista.html',{})

def send_email(mail):
  context = {'mail' : mail}
  #template = get_template('correo.html')
  content = template.render(context)

  email = EmailMultiAlternatives(
    'UN correo de prueba'
    'codigoFacilito'
    #settings.EMAIL_HOST_USER,
    [mail]
  )
  email.attach_alternative(content, 'text/html')
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
