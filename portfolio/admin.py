from django.contrib import admin
from .models import *

# Register your models here.
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'duracao','urlSite',)
    search_fields = ('nome',)
    ordering = ('nome',)

class DocenteAdmin(admin.ModelAdmin):
    list_display=('nome','email',)
    search_fields = ('nome',)
    ordering = ('nome',)

class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre', 'ects',)
    list_filter = ('ano', 'semestre',)
    search_fields = ('nome',)
    filter_horizontal = ('licenciaturas', 'docentes',)

class TecnologiaAdmin(admin.ModelAdmin):
    list_display=('nome','nivel',)
    search_fields=('nome',)
    list_filter = ('tipo',)
    ordering=('nome',)

class CategoriaCompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    ordering = ('nome',)

class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria',)
    list_filter = ('categoria',)
    search_fields = ('nome',)
    ordering = ('nome',)

class TfcAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'aluno', 'orientador', 'ano', 'classificacao')
    list_filter = ('ano', 'classificacao', 'licenciatura')
    search_fields = ('titulo', 'aluno', 'orientador')
    ordering = ('-classificacao', 'titulo')
    filter_horizontal = ('licenciatura', 'tecnologia')

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'uc')
    list_filter = ('tipo', 'uc')
    search_fields = ('titulo',)
    ordering = ('titulo',)
    filter_horizontal = ('tecnologias',)


class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'instituicao', 'data_inicio', 'data_conclusao')
    search_fields = ('titulo', 'instituicao')
    ordering = ('-data_inicio',)

class MakingOfAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'dataRegisto')
    list_filter = ('licenciatura', 'uc')
    search_fields = ('titulo',)
    ordering = ('-dataRegisto',)

admin.site.register(Licenciatura,LicenciaturaAdmin)
admin.site.register(Docente,DocenteAdmin)
admin.site.register(UnidadeCurricular,UnidadeCurricularAdmin)
admin.site.register(Tecnologia,TecnologiaAdmin)
admin.site.register(Competencia,CompetenciaAdmin)
admin.site.register(CategoriaCompetencia,CategoriaCompetenciaAdmin)
admin.site.register(Tfc,TfcAdmin)
admin.site.register(Projeto,ProjetoAdmin)
admin.site.register(Formacao,FormacaoAdmin)
admin.site.register(MakingOf,MakingOfAdmin)