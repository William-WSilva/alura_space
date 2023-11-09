from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'categoria', 'descricao', 'publicada') # campos exibidos na tabela
    list_display_links = ('id', 'nome') # campos clicaveis para editar
    search_fields = ('nome',) # campo de busca pelo campo nome
    list_filter = ('categoria',) # filtro rápido por categoria
    list_editable = ('publicada',)
    list_per_page = 10

admin.site.register(Fotografia, ListandoFotografias)
