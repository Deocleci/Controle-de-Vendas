from rest_framework import serializers

from controlevendas.models import Pedido, ProdutoQuantidadePedido, Cliente, Vendedor, Produto

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['numeroPedido']

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['Nome']

class ProdutoQuantidadePedidoSerializers(serializers.ModelSerializer):
    produto = ProdutoSerializer( read_only=True)
    pedido = PedidoSerializer( read_only=True)
    class Meta:
        model= ProdutoQuantidadePedido
        fields = ['id', 'quantidadeProduto','produto', 'pedido']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome']

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = ['nome']

class RelatorioSerializers(serializers.ModelSerializer):
    produtoquantidadepedido_set = ProdutoQuantidadePedidoSerializers(many=True, read_only=True)
    cliente = ClienteSerializer( read_only=True)
    vendedor = VendedorSerializer( read_only=True)
    class Meta:
        model= Pedido
        fields = ['id', 'numeroPedido','cliente', 'vendedor', 'valorTotal', 'dataCompra',  'produtoquantidadepedido_set']
        read_only_fields = ['valorTotal']