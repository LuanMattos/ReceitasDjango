from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:receita_id>', views.receita, name='receita'),
    path('buscar', views.buscar, name='buscar'),
    path('salvar_receita', views.salvar_receita, name='salvar_receita')
]