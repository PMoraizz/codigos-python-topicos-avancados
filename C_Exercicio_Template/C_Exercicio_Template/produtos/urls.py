from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.principal, name='principal'),
    path('produto/<int:id>/', views.produto, name='produto'),
]
