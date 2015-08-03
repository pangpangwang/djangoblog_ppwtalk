import os
import sys
import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application
sys.path.append(r'E:/django_blog')
#sys.path.append(r'E:/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_blog.settings'

application = get_wsgi_application()
