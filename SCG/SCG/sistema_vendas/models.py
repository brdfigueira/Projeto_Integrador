from django.db import models


class Cliente(models.Model):
    codigo = models.CharField(max_length=3)
    nome = models.CharField(max_length=100)
    documento_identidade = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14)

    def __str__(self):
        return self.nome


class Estoque(models.Model):
    nome_peca = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=0)
    valor_unitario = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome_peca