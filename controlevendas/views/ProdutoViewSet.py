from rest_framework.viewsets import  ModelViewSet
from controlevendas.serializers import ProdutoSerializers
from controlevendas.models import Produto
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from controlevendas.permissions import VendedorPermission

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializers
    permission_classes = [IsAuthenticated, VendedorPermission]
    authentication_classes = [TokenAuthentication]
    http_method_names = ['get', 'put', 'patch']