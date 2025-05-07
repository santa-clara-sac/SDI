from django.contrib import admin
from .models import CasoJudicial

@admin.register(CasoJudicial)
class CasoJudicialAdmin(admin.ModelAdmin):
    list_display = (
        'codigo',
        'expediente',
        'sede',
        'especialidad',
        'materia',
        'juzgado',
        'demandante',
        'demandado',
        'anio_inicio',
        'representante',
    )
    search_fields = ('expediente', 'demandante', 'demandado', 'juzgado')
    list_filter = ('sede', 'especialidad', 'materia', 'anio_inicio', 'representante')