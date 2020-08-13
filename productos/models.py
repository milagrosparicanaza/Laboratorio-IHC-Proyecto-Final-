from django.db import models
from django.urls import reverse
from vendedor.models import Vendedor

class Producto(models.Model):
  nombre = models.TextField(max_length = 100)
  precio = models.DecimalField(max_digits=7, decimal_places=2)
  descripcion = models.TextField(max_length = 250)
  foto =  models.ImageField(upload_to = 'fotoProducto/')
  vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
  # clientes = models.ManyToManyField(Cliente)
  def get_absolute_url(self):
    return reverse('productos:productos-detail', kwargs = {'pk': self.id})
