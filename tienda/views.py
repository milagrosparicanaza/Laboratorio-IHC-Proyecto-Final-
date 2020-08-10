from django.shortcuts import render
from django.http import HttpResponse
from productos.models import Producto

# Create your views here.
def homeView(request):
  data = {
    "name": "Gustavo",
    "productos": Producto.objects.all()
  }
  return render(request,"index.html", data)
