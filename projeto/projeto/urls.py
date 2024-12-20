from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.log, name='login'),
    path('login_responsavel/', views.loginPai, name='login_pai'),
    path('login_professor/', views.loginProfessor, name='login_professor'),
    path('admin/', admin.site.urls),
    path('responsavel/', views.homePai, name='home_pai'),
    path('home_professor/', views.homeProfessor, name='home_professor'),
    path('cadastrar_notas/<int:simulado_id>/', views.cadastrar_notas, name='cadastrar_notas'), # Corrigido aqui
    path('cadastrar_turma/', views.cadastrar_turma, name='cadastrar_turma'),
    path('cadastrar_aluno/<int:id>', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('turmas/', views.turmas, name='turmas'),
    path('alunos/<int:id>', views.alunos, name='alunos')
]
