from django.db import models
from datetime import datetime


class LoteFabricacao(models.Model):
    codigo = models.CharField('Código de Indentificação do lote', max_length=20, null=False, unique=True)
    dataFabricacao = models.DateField('Data de fabricação')
    quantidadeProduto = models.IntegerField('Quantidade de produtos', blank=False, default=0)

    dataCadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True, null=True)
    dataUltimaAlteracao = models.DateTimeField('Última alteração', null=True, blank=True, auto_now=True)

    class Meta:
        verbose_name = 'Lote de Fabricação'
        verbose_name_plural = 'Lotes de Fabricação'
        ordering = ['dataCadastro', ]

    def __str__(self):
        return f'{self.codigo} - {self.dataFabricacao}'