# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from controlevendas.models import Cliente, LoteFabricacao, Pedido, Produto, Vendedor, ProdutoQuantidadePedido

admin.site.register(Cliente)
admin.site.register(LoteFabricacao)
admin.site.register(Pedido)
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        'codigo',
        'Nome',
        'numeroLote',
        'cor',
        'descricao',
        'valor',

    ]
    fieldsets = [
        ("Dados principais", {
            'fields': ('codigo','Nome','numeroLote','cor','descricao','valor',),
        }),
        ]
admin.site.register(Vendedor)
admin.site.register(ProdutoQuantidadePedido)
