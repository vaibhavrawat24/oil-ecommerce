from django.core.wsgi import get_wsgi_application
import os
import manage

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

application = get_wsgi_application()

if __name__ == "__main__":
    manage.initialize()