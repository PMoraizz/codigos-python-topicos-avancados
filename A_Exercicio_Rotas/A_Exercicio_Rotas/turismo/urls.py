from django.urls import path
from . import views

app_name = 'turismo'

urlpatterns = [
    path('', views.home, name='home'),
    path('ponto/<str:nome>/', views.ponto, name='ponto'),
    path('redirecionar-prefeitura/', views.redirecionar_prefeitura, name='redirecionar_prefeitura'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),
]
