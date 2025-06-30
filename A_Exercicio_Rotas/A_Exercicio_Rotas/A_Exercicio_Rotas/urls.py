from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cidade/', include(('cidade.urls', 'cidade'))),
    path('turismo/', include(('turismo.urls', 'turismo'))),
]
