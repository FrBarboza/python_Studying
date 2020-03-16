from django.contrib import admin
from .models import Produto, Cliente


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'preco', 'estoque']
    ordering = ['nome']


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente)
