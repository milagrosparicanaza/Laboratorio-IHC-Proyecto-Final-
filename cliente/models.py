from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit_card  =      models.TextField(max_length = 20)
    def get_absolute_url(self):
        return reverse("cliente:cliente-detail", kwargs={"pk": self.pk})

