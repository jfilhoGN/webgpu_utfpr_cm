from django.db import models

# Create your models here.
class Exercicio(models.Model):
    numeroExercicio = models.CharField(max_length=4, blank=False)
    descricao = models.CharField(max_length=100, blank=False)
    codigo = models.CharField(max_length=1000, blank=False)
    resposta = models.CharField(max_length=100, blank=False)
    # Pesquisar como funciona ForeignKey
    #Usuario_idUsuario = models.ForeignKey(Usuario)

    def __str__(self):
        return self.numeroExercicio