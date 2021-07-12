from rest_framework.viewsets import  ModelViewSet
from controlevendas.serializers import PedidoSerializers, RelatorioSerializers
from controlevendas.models import Pedido
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from rest_framework.pagination import LimitOffsetPagination
from controlevendas.permissions import VendedorPermission

class RelatorioPedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = RelatorioSerializers
    permission_classes = [IsAuthenticated, VendedorPermission]
    authentication_classes = [TokenAuthentication]
    pagination_class = LimitOffsetPagination
    http_method_names = ['get']

    def get_queryset(self):
        opcao = self.request.query_params.get('orderby')
        if opcao == "valor":
            return  self.queryset.order_by('-valorTotal')
        if opcao == "data":
            return  self.queryset.order_by('dataCompra')

        return self.queryset



