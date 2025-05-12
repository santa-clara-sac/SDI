from django.urls import path
from . import views

app_name = 'control_expediente'

urlpatterns = [
    path('lista_expediente/', views.lista_expediente, name='lista_expediente'),
    path('editar_expediente/', views.editar_expediente, name='editar_expediente'),
    path('eliminar_expediente/<int:doc_id>/', views.eliminar_expediente, name='eliminar_expediente'),

    path('seguimiento/<int:caso_id>/', views.ver_seguimiento, name='ver_seguimiento'),
    path('editar_seguimiento/', views.editar_seguimiento, name='editar_seguimiento'),
    path('seguimiento/eliminar/<int:seguimiento_id>/', views.eliminar_seguimiento, name='eliminar_seguimiento'),

    path('editar_ce_gasto/', views.editar_gasto, name='editar_gasto'),
    path('eliminar_ce_gasto/', views.eliminar_gasto, name='eliminar_gasto'),

    path('seguimiento/<int:seguimiento_id>/gastos/', views.listar_gastos_por_seguimiento, name='listar_gastos'),

]