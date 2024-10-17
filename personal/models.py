from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50,blank=True)
    email = models.EmailField(blank=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Lembrete(models.Model):
    titulo = models.CharField(max_length=100,blank=True)
    descricao = models.TextField(blank=True)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        if self.titulo != "":
            return self.titulo
        else:
            return self.descricao[:10]