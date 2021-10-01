from django.contrib import admin
from .models import Contato, Categoria

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome','sobrenome','telefone','categoria_ctt','mostrar')
    list_display_links = ('id','nome','sobrenome')
    list_filter = ('nome','telefone')
    list_editable = ('telefone','mostrar')
    list_per_page = 10

admin.site.register(Contato,ContatoAdmin)
admin.site.register(Categoria)