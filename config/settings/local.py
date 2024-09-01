from .base import *
import sys

SECRET_KEY = 'django-insecure-ie$*t(a8b4r10#$a4_d4!sgra(__ai%0d@5!k=#1rf5+7@wt2*'
DEBUG = True

if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',  # Use an in-memory database for tests
    }