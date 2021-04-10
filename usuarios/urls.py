from django.urls import path

from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('cria/receita', views.cria_receita, name='cria_receita'),
    path('deletar_receita/<int:receita_id>', views.deletar_receita, name='deletar_receita'),
    path('editar_receita/<int:receita_id>', views.editar_receita, name='editar_receita'),
]