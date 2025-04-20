# admin.py

from django.contrib import admin
from .models import Responsable, Proyecto, Actividad, Gasto

@admin.register(Responsable)
class ResponsableAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'documento', 'correo', 'telefono', 'fecha_registro')
    search_fields = ('nombre_completo', 'documento', 'correo')

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'centro_de_costos', 'tipo_gasto', 'responsable', 'fecha_registro')
    search_fields = ('nombre', 'codigo')
    list_filter = ('tipo_gasto',)

@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('nombre_actividad', 'codigo_actividad', 'adicional', 'tipo_gasto', 'proyecto', 'fecha_inicio', 'fecha_fin')
    search_fields = ('nombre_actividad', 'codigo_actividad')
    list_filter = ('adicional', 'tipo_gasto')

@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('actividad', 'item', 'fecha', 'documento', 'fecha_registro')
    search_fields = ('item', 'documento')
    list_filter = ('fecha',)
