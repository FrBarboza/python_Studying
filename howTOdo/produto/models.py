from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    nota = models.TextField(blank=True, null=True, verbose_name='Descrição')
    tempo_validade = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'produto'

    def __str__(self):
        return self.nome

    def get_data_criacao(self):
        return self.data_criacao.strftime('%d/%m/%Y %H:%M')

    # caso necessite colocar a data na página HTML, esse é o formato
    # quando o formato do box está dateformat-local
    def get_data_input_criacao(self):
        return self.data_criacao.strftime('%Y-%m-%dT%H:%M')
