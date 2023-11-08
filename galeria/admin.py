from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'categoria', 'descricao') # campos exibidos na tabela
    list_display_links = ('id', 'nome') # campos clicaveis para editar
    search_fields = ('nome',) # campo de busca pelo campo nome
    list_filter = ('categoria',)

admin.site.register(Fotografia, ListandoFotografias)
