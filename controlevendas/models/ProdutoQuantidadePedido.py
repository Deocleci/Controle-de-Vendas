from django.db import models
from controlevendas.models import Produto
from controlevendas.models import Pedido

class ProdutoQuantidadePedido(models.Model):
    quantidadeProduto = models.IntegerField('Quantidade de produtos para pedido', blank=False, default=0)
    produto = models.ForeignKey(Produto, verbose_name='Produto',  editable=True, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, verbose_name='Pedido',  editable=True, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Quantidade'
        verbose_name_plural = 'Quantidades'
        ordering = ['quantidadeProduto', ]

    def __str__(self):
        return f'{self.produto} - {self.quantidadeProduto}'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.pedido.valorTotal = self.pedido.valorTotal + (self.produto.valor * self.quantidadeProduto)
            self.pedido.save()
        else:
            valorAnterior = self.pedido.produtoquantidadepedido_set.all().filter(pk=self.pk)[0]
            self.pedido.valorTotal = self.pedido.valorTotal - (valorAnterior.quantidadeProduto * valorAnterior.produto.valor)
            self.pedido.valorTotal = self.pedido.valorTotal  + (self.produto.valor * self.quantidadeProduto)
            self.pedido.save()
        super(ProdutoQuantidadePedido, self).save(*args, **kwargs)