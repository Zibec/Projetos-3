from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Responsavel/', views.homePai, name='home_pai'),
    path('cadastrar_notas/<int:simulado_id>/', views.cadastrar_notas, name='cadastrar_notas'),  # Corrigido aqui
    path('login_responsavel/', views.loginPai, name = 'login_responsavel'),
    path('login_professor/', views.loginProfessor, name = 'login_professor')
]
