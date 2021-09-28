from django.db import models
from django.utils import timezone

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao =models.TextField(blank=True)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True,upload_to='fotos/%Y/%m/')

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome_cat = models.CharField(max_length=255)     
    
    def __str__(self):
        return self.nome_cat   
