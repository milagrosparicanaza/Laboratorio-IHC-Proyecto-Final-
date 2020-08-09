from django.db import models
from django.urls import reverse

class Producto(models.Model):
  nombre = models.TextField(max_length = 80)
  precio = models.DecimalField(max_digits=7, decimal_places=2)
  descripcion = models.TextField(max_length = 80)
  foto =  models.TextField(max_length = 80)
  # vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
  # clientes = models.ManyToManyField(Cliente)
  def get_absolute_url(self):
    return reverse('tienda:producto-detail', kwargs = {'pk': self.id})
