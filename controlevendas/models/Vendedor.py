from django.db import models
from controlevendas.models import AbstractPessoa
from django.contrib.auth.models import User, Group


class Vendedor(AbstractPessoa):
    user = models.OneToOneField(User, verbose_name='Usuário', blank=True, null=True, editable=True,
                                on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'
        ordering = ['dataCadastro', ]

    def __str__(self):
        return self.nome
