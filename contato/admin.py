from django.contrib import admin
from .models import Contato, Categoria

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome','sobrenome','telefone','mostrar')
    list_display_links = ('id','nome','sobrenome')
    list_filter = ('nome','telefone')
    list_editable = ('telefone','mostrar')
    list_per_page = 10

admin.site.register(Contato,ContatoAdmin)