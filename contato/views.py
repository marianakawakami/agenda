from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.http import Http404


def index(request):
    contato = Contato.objects.all()
    return render(request,'index.html', {
        'contatos': contato
    })