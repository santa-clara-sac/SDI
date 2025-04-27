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

    path('agregar_nuevo_gasto/', views.agregar_nuevo_gasto, name='agregar_nuevo_gasto'),

    path('lista_gastoN1/', views.lista_gastoN1, name='lista_gastoN1'),
    path('editar_gastoN1/', views.editar_gastoN1, name='editar_gastoN1'),
    path('eliminar_gastoN1/<int:doc_id>/', views.eliminar_gastoN1, name='eliminar_gastoN1'),
    path('lista_gastoN2/', views.lista_gastoN2, name='lista_gastoN2'),
    path('editar_gastoN2/', views.editar_gastoN2, name='editar_gastoN2'),
    path('eliminar_gastoN2/<int:doc_id>/', views.eliminar_gastoN2, name='eliminar_gastoN2'),
    path('lista_gastoN3/', views.lista_gastoN3, name='lista_gastoN3'),
    path('editar_gastoN3/', views.editar_gastoN3, name='editar_gastoN3'),
    path('eliminar_gastoN3/<int:doc_id>/', views.eliminar_gastoN3, name='eliminar_gastoN3'),
]
