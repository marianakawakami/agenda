from django.urls import path
from . import views


urlpatterns = [
    #path('',views.index, name='index'),
    path('', views.ContatoIndex.as_view(), name='index'),
    path('categoria/<str:categoria>', views.ContatoCategoria.as_view(), name='contato_categoria'),
    path('busca/', views.ContatoBusca.as_view(), name='contato_busca'),
    path('contato/<int:pk>', views.ContatoDetalhes.as_view(), name='contato_detalhes')  
]