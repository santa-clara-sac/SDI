from django.urls import path
from . import views

app_name = 'centro_costos'

urlpatterns = [
    path('centro_costos_home/', views.centro_costos_home, name='centro_costos_home')    
]
