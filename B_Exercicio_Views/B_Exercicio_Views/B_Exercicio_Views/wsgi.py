import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'B_Exercicio_Views.settings')

application = get_wsgi_application()
