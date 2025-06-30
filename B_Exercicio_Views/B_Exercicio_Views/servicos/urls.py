from django.urls import path
from . import views

app_name = 'servicos'

urlpatterns = [
    path('calcular-desconto/', views.calcular_desconto, name='calcular_desconto'),
    path('mensagem/<str:usuario>/', views.mensagem_controle, name='mensagem_usuario'),
    path('maior/', views.maior, name='maior'),
    path('api-info/', views.api_info, name='api_info'),
]
