from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=25)
    email = models.CharField(max_length=60)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=255)
    status = models.CharField(max_length=20)