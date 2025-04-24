from django.urls import path
from . import views

app_name = 'centro_costos'

urlpatterns = [
    path('centro_costos_home/', views.centro_costos_home, name='centro_costos_home'),
    #path('lista_responsables/', views.lista_responsables, name='lista_responsables'),
    #path('editar_responsable/', views.editar_responsable, name='editar_responsable'),
    #path('eliminar_responsable/<int:doc_id>/', views.eliminar_responsable, name='eliminar_responsable'),

    path('lista_actividades/', views.lista_actividades, name='lista_actividades'),
    path('editar_actividad/', views.editar_actividad, name='editar_actividad'),
    path('eliminar_actividad/<int:doc_id>/', views.eliminar_actividad, name='eliminar_actividad'),
    
    path('lista_gastos/', views.lista_gastos, name='lista_gastos'),
    path('editar_gasto/', views.editar_gasto, name='editar_gasto'),
    path('eliminar_gasto/<int:doc_id>/', views.eliminar_gasto, name='eliminar_gasto'),

    path('lista_canta_callao/', views.lista_canta_callao, name='lista_canta_callao'),
    path('editar_canta_callao/', views.editar_canta_callao, name='editar_canta_callao'),
    path('eliminar_canta_callao/<int:doc_id>/', views.eliminar_canta_callao, name='eliminar_canta_callao'),

    path('lista_gasto_general/', views.lista_gasto_general, name='lista_gasto_general'),
    path('editar_gasto_general/', views.editar_gasto_general, name='editar_gasto_general'),
    path('eliminar_gasto_general/<int:doc_id>/', views.eliminar_gasto_general, name='eliminar_gasto_general'),
]
