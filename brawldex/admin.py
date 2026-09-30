from django.contrib import admin
from .models import Brawler


@admin.register(Brawler)
class BrawlerAdmin(admin.ModelAdmin):
    list_display = ('nome', 'raridade', 'classe', 'vida', 'dano')
    search_fields = ('nome', 'raridade', 'classe')
    list_filter = ('raridade', 'classe')

    fieldsets = (
        ('Informações básicas', {
            'fields': ('nome', 'raridade', 'classe', 'descricao')
        }),
        ('Atributos', {
            'fields': ('vida', 'dano')
        }),
        ('Imagem', {
            'fields': ('imagem', 'imagem_url'),
            'description': (
                'Se você enviar um arquivo em "imagem", ele tem prioridade. '
                'Caso contrário, o site usa a "URL da imagem".'
            )
        }),
    )   