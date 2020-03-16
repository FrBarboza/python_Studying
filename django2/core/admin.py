from django.contrib import admin

from .models import Produto


# Registro com decorator
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'preco', 'slug', 'estoque', 'criado', 'modificado', 'ativo']

# Registro sem decorator
# admin.site.register(Produto, ProdutoAdmin)
