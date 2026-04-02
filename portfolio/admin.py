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


admin.site.register(Licenciatura,LicenciaturaAdmin)
admin.site.register(Docente,DocenteAdmin)
admin.site.register(UnidadeCurricular,UnidadeCurricularAdmin)

