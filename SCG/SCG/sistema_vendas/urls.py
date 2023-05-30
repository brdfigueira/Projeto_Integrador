from django.contrib import admin
from django.urls import path
from . import views

app_name = "sistema_vendas"
urlpatterns = [
    path('pagina_inicial', views.pagina_inicial, name='pagina_inicial'),
    path('cadastrar_cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('entrada_estoque/', views.entrada_estoque, name='entrada_estoque'),
    path('consultar_estoque/', views.consultar_estoque, name='consultar_estoque'),
    path('realizar_venda/', views.realizar_venda, name='realizar_venda'),
]