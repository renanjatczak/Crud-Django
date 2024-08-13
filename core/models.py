from django.db import models # type: ignore

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=100)
    profissao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
