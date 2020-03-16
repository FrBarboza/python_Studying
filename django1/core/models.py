from django.db import models

# Create your models here.


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade')

    class Meta:
        db_table = 'produto'

    def __str__(self):
        # return f'{self.nome} --------- {self.estoque}'
        return {self.nome}


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    class Meta:
        db_table = 'cliente'

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

