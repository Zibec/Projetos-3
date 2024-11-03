from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cadastrar_notas/<int:simulado_id>/', views.cadastrar_notas, name='cadastrar_notas'),  # Corrigido aqui
]
