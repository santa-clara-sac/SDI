from django.contrib import admin
from .models import CentroDeCostos, TipoDeGasto, Actividad, Gasto, CantaCallao

@admin.register(CentroDeCostos)
class CentroDeCostosAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(TipoDeGasto)
class TipoDeGastoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'centro_de_costos', 'tipo', 'responsable', 'fecha_registro')
    list_filter = ('tipo', 'centro_de_costos')
    search_fields = ('nombre', 'codigo', 'responsable')

@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('actividad', 'fecha', 'documento', 'debe', 'haber', 'tipo_gasto', 'fecha_registro')
    list_filter = ('actividad', 'tipo_gasto', 'fecha')
    search_fields = ('nombre', 'detalle', 'documento')

@admin.register(CantaCallao)
class CantaCallaoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'fecha', 'referencia', 'monto1', 'monto2')
    search_fields = ('codigo', 'detalle', 'referencia')
    list_filter = ('fecha',)
