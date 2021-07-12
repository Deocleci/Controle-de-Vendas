
from django.urls import path
#####
from django.urls import path
from rest_framework import routers
from controlevendas.views import ProdutoViewSet, PedidoViewSet, RelatorioPedidoViewSet
from  rest_framework.authtoken.views import obtain_auth_token

router = routers.SimpleRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'relatorio', RelatorioPedidoViewSet)
# router.register(r'reports/employees', ReportsEmployeesViewSet)



app_name = 'controlevendas'

urlpatterns =[
    path('api-token-auth/', obtain_auth_token),
]

urlpatterns+=router.urls