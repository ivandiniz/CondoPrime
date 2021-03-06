# -*- encoding: utf8 -*-
from django.contrib import admin
from .models import Bloco, Unidade, Condominio, Espaco, Chave

# Register your models here.


class UnidadeInline(admin.TabularInline):
    model = Unidade
    extra = 8


class BlocoInLine(admin.TabularInline):
    model = Bloco
    extra = 2


class ChaveInLine(admin.TabularInline):
    model = Chave
    extra = 1


class CondominioAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informações do Condomínio', {'fields': ['nome', 'cnpj', 'tipo', 'finalidade', 'telefone']}),
        ('Endereço', {'fields': ['cep', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'estado']}),
    ]
    inlines = [BlocoInLine]


class BlocoAdmin(admin.ModelAdmin):
    fields = ['nome', 'condominio']
    inlines = [UnidadeInline]

    list_display = ['nome', 'condominio']
    list_filter = ['condominio']


class UnidadeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informações da Unidade', {'fields': ['bloco', 'numero']}),
        ('Informações do Proprietário', {'fields': ['proprietario']})
    ]

    list_display = ['numero', 'bloco', 'proprietario']
    list_filter = ['bloco']
    search_fields = ['numero']


class EspacoAdmin(admin.ModelAdmin):
    fields = ['nome', 'lotacao', 'regras', 'tem_controle_chave']
    inlines = [ChaveInLine]

    list_display = ['nome', 'lotacao', 'tem_controle_chave']
    search_fields = ['nome']


admin.site.register(Bloco, BlocoAdmin)
admin.site.register(Unidade, UnidadeAdmin)
admin.site.register(Condominio, CondominioAdmin)
admin.site.register(Espaco, EspacoAdmin)
admin.site.register(Chave)