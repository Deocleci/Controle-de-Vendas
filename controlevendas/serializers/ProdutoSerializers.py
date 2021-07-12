from rest_framework import serializers

from controlevendas.models import Produto



class ProdutoSerializers(serializers.ModelSerializer):

    class Meta:
        model= Produto
        fields = ['id', 'Nome', 'codigo', 'cor','getNumeroLote', 'descricao', 'valor']
