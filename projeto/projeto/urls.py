from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('cadastrar_nota/', views.cadastrar_nota, name='cadastrar_nota'),
]
