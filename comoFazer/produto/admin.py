from django.contrib import admin
from produto.models import Produto


# Register your models here.


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'nota', 'data_criacao')
    # list_filter = ('nome',)
    list_filter = ('usuario',)


admin.site.register(Produto, ProdutoAdmin)
