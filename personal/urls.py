from django.urls import path
from .views import * 

urlpatterns = [
    #contatos
    path('contatos/',ContatoListView.as_view(), name='contato_list' ),
    path('contato/<int:pk>/',ContatoDetailView.as_view(), name='contato_detail'),
    path('contato/novo/',ContatoCreate.as_view(), name='contato_create'),
    path('contato/<int:pk>/editar/',ContatoUpdateView.as_view(),name='contato_update'),
    path('contato/<int:pk>/deletar/',ContatoDeleteView.as_view(), name='contato_delete'),

    #lembretes
    path('lembretes/',LembreteListView.as_view(), name='lembrete_list' ),
    path('lembrete/<int:pk>/',LembreteDetailView.as_view(), name='lembrete_detail'),
    path('lembrete/novo/',LembreteCreate.as_view(), name='lembrete_create'),
    path('lembrete/<int:pk>/editar/',LembreteUpdateView.as_view(),name='lembrete_update'),
    path('lembrete/<int:pk>/deletar/',LembreteDeleteView.as_view(), name='lembrete_delete'),

]
