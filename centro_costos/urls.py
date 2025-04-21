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
]
