from django.contrib import admin
from .models import CasoJudicial, Seguimiento, Gasto, Presentacion, GastoPresentacion


class GastoInline(admin.TabularInline):
    model = Gasto
    extra = 1


class SeguimientoInline(admin.TabularInline):
    model = Seguimiento
    extra = 1


@admin.register(CasoJudicial)
class CasoJudicialAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'expediente', 'sede', 'juzgado', 'representante', 'anio_inicio')
    list_filter = ('representante', 'sede', 'especialidad', 'materia', 'anio_inicio')
    search_fields = ('expediente', 'demandante', 'demandado', 'juzgado')
    inlines = [SeguimientoInline]


@admin.register(Seguimiento)
class SeguimientoAdmin(admin.ModelAdmin):
    list_display = ('caso', 'fecha_seguimiento', 'responsable', 'estado')
    list_filter = ('estado', 'fecha_seguimiento')
    search_fields = ('caso__expediente', 'responsable', 'resolucion', 'seguimiento')
    inlines = [GastoInline]


@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('seguimiento', 'fecha', 'detalle', 'gastos_soles', 'gastos_dolares')
    list_filter = ('fecha',)
    search_fields = ('detalle', 'sustento')


@admin.register(Presentacion)
class PresentacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'caso', 'fecha', 'presentado', 'escrito')
    list_filter = ('fecha', 'presentado')
    search_fields = ('caso__expediente', 'presentado', 'escrito')

@admin.register(GastoPresentacion)
class GastoPresentacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'presentacion', 'fecha', 'detalle')  # Correcto: usamos 'presentacion'
    list_filter = ('fecha',)
    search_fields = ('detalle', 'presentacion__caso__expediente')  # Corregido aquí también