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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria'] = Categoria.objects.all()
        return context

class ContatoDetalhes(UpdateView):
    template_name = 'contato/contato_detalhes.html'
    form_class = Contato
    context_object_name = 'contato'

#def index(request):
#    contato = Contato.objects.all()
#    return render(request,'contato/index.html', {
#        'contatos': contato
#    })

