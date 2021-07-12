from rest_framework.viewsets import  ModelViewSet
from controlevendas.serializers import PedidoSerializers
from controlevendas.models import Pedido
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from rest_framework.pagination import LimitOffsetPagination
from controlevendas.permissions import VendedorPermission

class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializers
    permission_classes = [IsAuthenticated, VendedorPermission]
    authentication_classes = [TokenAuthentication]
    pagination_class = LimitOffsetPagination
    http_method_names = ['get', 'put', 'patch']

