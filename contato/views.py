from django.shortcuts import render, get_object_or_404
from .models import Contato, Categoria
from django.views.generic.list import ListView
from django.db.models import Q
from django.http import Http404


class ContatoIndex(ListView):
    model = Contato
    template_name = 'contato/index.html'
    paginate_by = 3
    context_object_name = 'contato'
    ordering = ['nome']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria'] = Categoria.objects.all()
        return context


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
    template_name = 'contato/contato_busca.html'

    def get_queryset(self):
        qs = super().get_queryset()

        categoria = self.kwargs.get('categoria', None)

        if not categoria:
            return qs

        qs = qs.filter(categoria_ctt__nome_cat__iexact=categoria)

        return qs