from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nome_cat = models.CharField(max_length=20,verbose_name="Categoria")

    def __str__(self):
        return self.nome_cat

class Contato(models.Model):
    nome = models.CharField(max_length=255,verbose_name='Nome')
    sobrenome = models.CharField(max_length=255, blank=True,verbose_name='Sobrenome')
    telefone = models.CharField(max_length=255,verbose_name='Telefone')
    email = models.CharField(max_length=255, blank=True,verbose_name='E-mail')
    data_criacao = models.DateTimeField(default=timezone.now,verbose_name='Data inclusão')
    descricao =models.TextField(blank=True,verbose_name='Observações')
    mostrar = models.BooleanField(default=True,verbose_name='Mostrar CTT')
    foto = models.ImageField(blank=True,null=True,upload_to='fotos/%Y/%m/',verbose_name='Foto')
    categoria_ctt = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING,
                                      blank=True, null=True, verbose_name='Categoria')

    def __str__(self):
        return self.nome