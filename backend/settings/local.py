from .base import *

DEBUG = True
# DATABASES = {
#     'default': {
#         'ENGINE': os.getenv('ENGINE'),
#         'NAME': os.getenv('NAME'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / '../db.sqlite3',
    }
}