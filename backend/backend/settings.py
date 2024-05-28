"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
from datetime import timedelta
from common.utils import PYPY_AVAILABLE as check_pypy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!5xe$b7a9e4osw_3i23&&f1_s$inz*=j#97-6z88sf!!(f6w2q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

STATIC_BULK_FOLDER = Path('./temp/bulk')

ASYNC_GENERATION = True
PYPY_AVAILABLE = check_pypy

VERSION = os.getenv('VERSION', 'dev')

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = [
    'http://localhost',
    'http://localhost:3000',
    'https://*.ngrok.io',
]
CORS_ALLOWED_ORIGIN_REGEXES = [
    r'https?://localhost:\d+',
    r'https?://127.0.0.1:\d+',
]
SOCIAL_AUTH_ALLOWED_REDIRECT_HOSTS = [
    'localhost',
    'localhost:3000',
    '127.0.0.1',
    'dev.commanderspellbook.com',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'social_django',
    'backend',
    'spellbook',
    'website',
    'django.contrib.admin',
    'adminsortable2',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'django_filters',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'djangorestframework_camel_case.middleware.CamelCaseMiddleWare',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'backend.templates.context.add_version_to_context',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Social Auth PostgresSQL settings
# https://python-social-auth.readthedocs.io/en/latest/configuration/django.html#database
SOCIAL_AUTH_JSONFIELD_ENABLED = True


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Discord Webhook(s)
# https://discord.com/developers/docs/resources/webhook
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL', None)


# Python Social Auth
# https://python-social-auth.readthedocs.io/en/latest/backends/index.html
SOCIAL_AUTH_DISCORD_KEY = os.getenv('DISCORD_CLIENTID', None)
SOCIAL_AUTH_DISCORD_SECRET = os.getenv('DISCORD_CLIENTSECRET', None)

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'last_name', 'email']
SOCIAL_AUTH_STRATEGY = 'backend.login.jwt.SimpleJwtDjangoStrategy'
SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ['code']
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_ERROR_URL = 'https://commanderspellbook.com/login/error'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
] + (
    ['backend.login.discord.DiscordOAuth2'] if SOCIAL_AUTH_DISCORD_KEY else []
)

# Simple JWT
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'UPDATE_LAST_LOGIN': True,
    'ISSUER': 'spellbook',
    'LEEWAY': timedelta(seconds=5),
    'TOKEN_OBTAIN_SERIALIZER': 'backend.login.jwt.TokenObtainPairSerializer',
}

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'djangorestframework_camel_case.parser.CamelCaseFormParser',
        'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_PAGINATION_CLASS': 'backend.pagination.CustomPagination',
    'PAGE_SIZE': 100,
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'timestamp': {
            'format': '[{levelname}] {asctime}: {message}',
            'style': '{'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'timestamp'
        },
    },
    'loggers': {
        # 'root': {
        #     'level': 'DEBUG',
        #     'handlers': ['console'],
        # },
        'root': {
            'level': 'INFO',
            'handlers': ['console'],
        },
        # 'django.db.backends': {
        #     'level': 'DEBUG',
        # },
    }
}
