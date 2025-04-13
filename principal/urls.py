from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    path('lista_usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('editar_usuario/', views.editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('cambiar_password_usuario/', views.cambiar_password_usuario, name='cambiar_password_usuario'),


    path('', include('partidas_planos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
