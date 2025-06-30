from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('cadastro/', views.cadastro_usuario, name='cadastro_usuario'),
    path('perfil/<str:usuario>/', views.perfil_usuario, name='perfil_usuario'),
    path('rota-atual/', views.mostrar_rota, name='mostrar_rota'),
]
