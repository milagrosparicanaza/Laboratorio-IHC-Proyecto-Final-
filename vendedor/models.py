from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Vendedor(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  tienda = models.CharField(max_length=100)
  def get_absolute_url(self):
    return reverse('vendedor:vendedor-detail', kwargs = {'pk': self.id})
  def __str__(self):
    return self.user.username
