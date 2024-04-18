from django.core.management.utils import get_random_secret_key
from pathlib import Path
import environ

# See https://docs.djangoproject.com/en/4.2/

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env(BASE_DIR / '.env')

SECRET_KEY =  env.str('DJANGO_SECRET_KEY', get_random_secret_key())

DEBUG = env.bool('DJANGO_DEBUG', False)

USE_SQLITE = env.bool('USE_SQLITE', True)

SQLITE_DB_NAME = env.str('SQLITE_DB_NAME')

ALLOWED_HOSTS = [env.str('ALLOWED_HOSTS', '*')]

INSTALLED_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django.contrib.sites',
    # Apps
    'main',
    'users',
    'goods',
    'carts',
    'orders',
    # Installs
    'debug_toolbar',
    'phonenumber_field',
    'django_recaptcha',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Apps
    'main.middleware.LogerMiddleware',
    # Installs
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'app.urls'

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
                # Apps
                'main.context_processors.base_processors',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend',]

WSGI_APPLICATION = 'app.wsgi.application'

# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if USE_SQLITE:
    DEFAULT_DATABASE = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / SQLITE_DB_NAME,
    }
else:
    DEFAULT_DATABASE = {
        'ENGINE': env.str('DB_ENGINE'),
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PASSWORD'),
        'HOST': env.str('DB_HOST'),
        'PORT': env.str('DB_PORT'),
    }

DATABASES = { 'default': DEFAULT_DATABASE }

# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
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

LANGUAGE_CODE = 'uk-ua'
TIME_ZONE = 'Europe/Kiev'
USE_I18N = True
USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = (BASE_DIR / 'static',)

INTERNAL_IPS = []

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': BASE_DIR / 'media/cache',
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'
LOGIN_URL = 'user:login'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env.str('EMAIL_HOST', '')
EMAIL_HOST_USER = env.str('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD', '')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

RECAPTCHA_PUBLIC_KEY = env.str('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = env.str('RECAPTCHA_PRIVATE_KEY')
RECAPTCHA_DOMAIN = env.str('RECAPTCHA_DOMAIN')

# Custom vars
SITE_TITLE = env.str('SITE_TITLE', 'Site')
GOODS_IN_PAGE = 6
