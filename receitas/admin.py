from django.contrib import admin
from .models import Receita

class ListandoReceitas(admin.ModelAdmin):
    configuracao = ('id', 'nome_receita', 'categoria')
    list_display =  configuracao
    list_display_links = configuracao
    search_fields = ('id','nome_receita')
    list_filter = ['categoria']
    list_per_page = 5


admin.site.register(Receita, ListandoReceitas)
