from django.urls import path
from . import views

app_name = 'control_expediente'

urlpatterns = [
    path('lista_expediente/', views.lista_expediente, name='lista_expediente'),
    path('editar_expediente/', views.editar_expediente, name='editar_expediente'),
    path('eliminar_expediente/<int:doc_id>/', views.eliminar_expediente, name='eliminar_expediente'),

     path('seguimiento/<int:caso_id>/', views.ver_seguimiento, name='ver_seguimiento'),
]