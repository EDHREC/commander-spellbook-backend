import os
import sys
from .settings import *  # noqa: F403
from .settings import BASE_DIR, REST_FRAMEWORK

TESTING = sys.argv[1:2] == ['test']

SECRET_KEY = os.environ['SECRET_KEY'] if not TESTING else "test"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Security settings
ALLOWED_HOSTS = [
    '.commanderspellbook.com',
    'localhost'
]

CSRF_TRUSTED_ORIGINS = [
    'https://*.commanderspellbook.com',
    'http://localhost',
]

SOCIAL_AUTH_ALLOWED_REDIRECT_HOSTS = [
    'commanderspellbook.com',
    'localhost',
    'dev.commanderspellbook.com'
]

# Reverse proxy settings
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Pod settings
POD_IP = os.getenv('THIS_POD_IP', None)
if POD_IP is not None:
    ALLOWED_HOSTS.append(POD_IP)

# Production settings
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_BULK_FOLDER = STATIC_ROOT / 'bulk'
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CONN_MAX_AGE = 60 * 60

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': os.getenv('KUBE_SQL_ENGINE', os.getenv('SQL_ENGINE', 'django.db.backends.sqlite3')),
        'NAME': os.getenv('KUBE_SQL_DATABASE', os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3"))),
        "USER": os.getenv('KUBE_SQL_USER', os.environ.get("SQL_USER", "user")),
        "PASSWORD": os.getenv('KUBE_SQL_PASSWORD', os.environ.get("SQL_PASSWORD", "password")),
        "HOST": os.getenv('KUBE_SQL_HOST', os.environ.get("SQL_HOST", "localhost")),
        "PORT": os.getenv('KUBE_SQL_PORT', os.environ.get("SQL_PORT", "5432")),
    }
}

REST_FRAMEWORK = {
    **REST_FRAMEWORK,
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/minute',
        'user': '1000/minute'
    }
}

if TESTING:
    REST_FRAMEWORK['DEFAULT_THROTTLE_RATES'] = {
        "anon": "10000/minute",
        "user": "10000/minute",
    }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
