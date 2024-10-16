from .models import Contato
from django import forms 

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'

        label = {
            "nome":"Nome",
            "telefone" : "Telefone",
            "email" : "E-mail",
            "descricao" : "Descrição",
        }

        widgets = {
            "nome": forms.TextInput(attrs={"placeholder":"Nome"}),
            "telefone": forms.TextInput(attrs={"placeholder":"Telefone"}),
            "email": forms.TextInput(attrs={"placeholder":"E-mail"}),
            "descricao": forms.TextInput(attrs={"placeholder":"Descrição"}),
        }