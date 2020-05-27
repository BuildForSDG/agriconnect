# coding=utf-8
"""
The test settings for AgriConnect.
"""
from .settings import *

DEBUG = True

# Overriding logging to avoid file issues
LOGGING = {}

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db-test.sqlite3'),
	}
}
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
