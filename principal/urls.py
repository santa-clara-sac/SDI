from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    path('lista_usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('editar_usuario/', views.editar_usuario, name='editar_usuario'),
    path('editar_CC/', views.editar_CC, name='editar_CC'),
    path('eliminar_CC/<int:id>/', views.eliminar_CC, name='eliminar_CC'),
    path('eliminar_usuario/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('cambiar_password_usuario/', views.cambiar_password_usuario, name='cambiar_password_usuario'),

    path('', include('partidas_planos.urls')),
    path('', include('centro_costos.urls')),
    path('', include('control_expediente.urls')),
    path('', include('hoja_requerimiento.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
