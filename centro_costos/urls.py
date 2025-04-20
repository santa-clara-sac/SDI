from django.urls import path
from . import views

app_name = 'centro_costos'

urlpatterns = [
    path('centro_costos_home/', views.centro_costos_home, name='centro_costos_home'),
    path('lista_responsables/', views.lista_responsables, name='lista_responsables'),
    path('editar_responsable/', views.editar_responsable, name='editar_responsable'),
    path('eliminar_responsable/<int:doc_id>/', views.eliminar_responsable, name='eliminar_responsable'),

    path('lista_proyectos/', views.lista_proyectos, name='lista_proyectos'),
    path('editar_proyecto/', views.editar_proyecto, name='editar_proyecto'),
]
