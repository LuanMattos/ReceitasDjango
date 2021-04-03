from django.contrib import admin
from .models import Pessoa

class ListaPessoas(admin.ModelAdmin):
    configuracao = ('nome','email')
    list_display =  configuracao
    list_display_links = configuracao
    search_fields = ('nome','email')

admin.site.register(Pessoa, ListaPessoas)
