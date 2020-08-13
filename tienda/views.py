from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from productos.models import Producto
from vendedor.models import Vendedor
from django.contrib.auth.views import LoginView, LogoutView
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

class homeView(ListView):
  model = Producto
  template_name = 'index.html'
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user = self.request.user.id
    print(user)
    if user != None:
    	context['Vendedor'] = Vendedor.objects.get(user__id = user)
    	print(context['Vendedor'])
    context['name'] = 'Gustavo'
    return context

class LoginFormView(LoginView):
  template_name = 'login.html'
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Iniciar sesion'
    return context

def send_email(mail):
  context = {'mail': mail}

  template = get_template('correo.html')
  content = template.render(context)

  email = EmailMultiAlternatives(
    'Este es un correo de Prueba',
    'Desde Django',
    settings.EMAIL_HOST_USER,
    [mail]
  )
  
  email.attach_alternative(content, 'text/html')
  email.send


def email(request):
  if request.method == 'POST':
    mail = request.POST.get('mail')
    send_email(mail)
  return render(request, 'send_mail.html', {})
