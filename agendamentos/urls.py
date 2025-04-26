from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='clientes_listar'),
    path('adicionar/', views.adicionar_cliente, name='adicionar_cliente'),
    path('atualizar/<int:pk>/', views.atualizar_cliente, name='atualizar_cliente'),
    path('deletar/<int:pk>/', views.deletar_cliente, name='deletar_cliente'),
]
