from django.urls import path
from . import views

app_name = 'cidade'

urlpatterns = [
    path('', views.home, name='home'),
    path('bairro/<str:nome>/', views.bairro, name='bairro'),
    path('prefeitura/', views.prefeitura, name='prefeitura_padrao'),
    path('prefeitura/<str:prefeito>', views.prefeitura, name='prefeitura'),
]
