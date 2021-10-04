from django.shortcuts import render
from .models import Contato,Categoria
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.db.models import Q, Count, Case, When
from django.contrib import messages

class ContatoIndex(ListView):
    model = Contato
    template_name ='contato/index.html'
    paginate_by = 3
    context_object_name = 'contato'
    ordering = ['nome']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria'] = Categoria.objects.all()
        return context

class ContatoDetalhes(UpdateView):
    template_name = 'contato/contato_detalhes.html'
    form_class = Contato
    context_object_name = 'contato'

class ContatoBusca(ContatoIndex):
    template_name = 'contato/contato_busca.html'

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')

        if not termo:
            return qs

        qs = qs.filter(
            Q(nome__icontains=termo) |
            Q(sobrenome__icontains=termo) |
            Q(categoria_ctt__nome_cat__iexact=termo)
        )

        return qs

class ContatoCategoria(ContatoIndex):
    template_name = 'contato/index.html'

    def get_queryset(self):
        qs = super().get_queryset()

        categoria = self.kwargs.get('categoria', None)

        if not categoria:
            return qs

        qs = qs.filter(categoria_ctt__nome_cat__iexact=categoria)

        return qs        