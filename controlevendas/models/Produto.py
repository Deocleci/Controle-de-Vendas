from django.db import models
from controlevendas.models import LoteFabricacao

class Produto(models.Model):
    codigo = models.CharField('Código de Indentificação do produto', max_length=20, null=False, unique=True)
    Nome = models.CharField('Nome do produto', max_length=255)
    numeroLote = models.ForeignKey(LoteFabricacao, verbose_name='Lote de fabricação do produto',  editable=True, on_delete=models.CASCADE)
    cor = models.CharField('Cor do produto', max_length=20, null=False)
    descricao = models.TextField("Descrição do produto", blank=True)
    valor = models.DecimalField('Valor do produto', max_digits=9, decimal_places= 2, null=True)

    dataCadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True, null=True)
    dataUltimaAlteracao = models.DateTimeField('Última alteração', null=True, blank=True, auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['dataCadastro', ]

    def __str__(self):
        return self.Nome

    def getNumeroLote(self):
        return self.numeroLote.codigo