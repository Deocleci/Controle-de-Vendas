from django.db import models
from controlevendas.models import AbstractPessoa

class Cliente(AbstractPessoa):

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['dataCadastro', ]

    def __str__(self):
        return self.nome