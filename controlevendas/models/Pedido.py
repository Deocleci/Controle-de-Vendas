from django.db import models
from controlevendas.models import Cliente, Vendedor


class Pedido(models.Model):
    numeroPedido = models.IntegerField('Número do pedido', blank=False)
    cliente = models.ForeignKey(Cliente, verbose_name='Cliente', on_delete=models.PROTECT)
    vendedor = models.ForeignKey(Vendedor, verbose_name='Vendedor', on_delete=models.PROTECT)
    valorTotal = models.DecimalField('Valor total do Pedido', max_digits=9, decimal_places= 2, default=0)

    dataCompra = models.DateTimeField('Data de Compra', auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['dataCompra', ]

    def __str__(self):
        return f'{self.numeroPedido}'
