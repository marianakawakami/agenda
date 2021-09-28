from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.http import Http404


def index(request):
    contato = Contato.objects.all()
    paginator = Paginator(contato, 20)  # Show 25

    page = request.GET.get('p')
    contato = paginator.get_page(page)

    return render(request,'index.html', {
        'contatos': contato
    })