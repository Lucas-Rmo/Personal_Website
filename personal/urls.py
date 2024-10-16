from django.urls import path
from .views import * 

urlpatterns = [
    path('contatos/',ContatoListView.as_view(), name='contato_list' ),
    path('contato/<int:pk>/',ContatoDetailView.as_view(), name='contato_detail'),
    path('contato/novo/',ContatoCreate.as_view(), name='contato_create'),
    path('contato/<int:pk>/editar/',ContatoUpdateView.as_view(),name='contato_update'),
    path('contato/<int:pk>/deletar/',ContatoDeleteView.as_view(), name='contato_delete')

]
