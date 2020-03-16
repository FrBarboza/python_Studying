from django.contrib import admin
from estoque.models import Estoque


# Register your models here.


class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'nota', 'data_criacao')
    # list_filter = ('nome',)
    list_filter = ('usuario',)


admin.site.register(Estoque, EstoqueAdmin)
