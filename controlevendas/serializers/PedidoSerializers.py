from rest_framework import serializers

from controlevendas.models import Pedido, ProdutoQuantidadePedido
from controlevendas.serializers import ProdutoSerializers

class ProdutoQuantidadePedidoSerializers(serializers.ModelSerializer):
    # produto_set = ProdutoSerializers(many=True, read_only=True)

    class Meta:
        model= ProdutoQuantidadePedido
        fields = ['id', 'quantidadeProduto','produto', 'pedido']

class PedidoSerializers(serializers.ModelSerializer):
    produtoquantidadepedido_set = ProdutoQuantidadePedidoSerializers(many=True, read_only=True)

    class Meta:
        model= Pedido
        fields = ['id', 'numeroPedido','cliente', 'vendedor', 'valorTotal', 'dataCompra',  'produtoquantidadepedido_set']
        read_only_fields = ['valorTotal']