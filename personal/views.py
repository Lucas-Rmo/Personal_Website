from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView
from .models import *
from .forms import *

# Create your views here.

#CONTATOS
#criação de contatos
class ContatoCreate(CreateView):
    model = Contato
    form_class = ContatoForm
    template_name = 'agenda/contato_form.html'
    success_url = reverse_lazy('contato_list')


#listar os contatos
class ContatoListView(ListView):
    model = Contato
    template_name = 'agenda/contato_list.html'
    context_object_name = 'contatos'

#exibir os detalhes de um único contato
class ContatoDetailView(DetailView):
    model = Contato
    template_name = 'agenda/contato_detail.html'
    context_object_name = 'contato'

#atualização de um contato
class ContatoUpdateView(UpdateView):
    model = Contato
    form_class = ContatoForm
    template_name = 'agenda/contato_form.html'
    success_url = reverse_lazy('contato_list')

class ContatoDeleteView(DeleteView):
    model = Contato
    template_name = 'agenda/contato_confirm_delete.html'
    success_url = reverse_lazy('contato_list')



#LEMBRETES
#criação de contatos
class LembreteCreate(CreateView):
    model = Lembrete
    form_class = LembreteForm
    template_name = 'lembretes/lembrete_form.html'
    success_url = reverse_lazy('lembrete_list')


#listar os lembretes
class LembreteListView(ListView):
    model = Lembrete
    template_name = 'lembretes/lembrete_list.html'
    context_object_name = 'lembretes'

#exibir os detalhes de um único lembrete
class LembreteDetailView(DetailView):
    model = Lembrete
    template_name = 'lembretes/lembrete_detail.html'
    context_object_name = 'lembrete'

#atualização de um lembrete
class LembreteUpdateView(UpdateView):
    model = Lembrete
    form_class = LembreteForm
    template_name = 'lembretes/lembrete_form.html'
    success_url = reverse_lazy('lembrete_list')

#excluir lembrete
class LembreteDeleteView(DeleteView):
    model = Lembrete
    template_name = 'lembretes/lembrete_confirm_delete.html'
    success_url = reverse_lazy('lembrete_list')


