import os, environ
from pathlib import Path
from django.conf.global_settings import AUTH_USER_MODEL, EMAIL_BACKEND, EMAIL_USE_SSL, EMAIL_USE_TLS

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =  env.str('DJANGO_SECRET_KEY', default='')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', default=False)

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    # Apps
    "main",
    "goods",
    "users",
    "carts",
    "orders",
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "django.contrib.sites",
    # Installs
    'debug_toolbar',
    'phonenumber_field',
    'captcha',
    # 'django_recaptcha',  
    # "allauth",
    # "allauth.account",
    # "allauth.socialaccount",
    # 'allauth.socialaccount.providers.google',
]

# django_recaptcha
RECAPTCHA_PUBLIC_KEY = '6LfBz6IpAAAAAC5Avijv_rOp7IXuWU26WLUQQgVp'
RECAPTCHA_PRIVATE_KEY = '6LfBz6IpAAAAAC5Avijv_rOp7IXuWU26WLUQQgVp'
# RECAPTCHA_DOMAIN = 'www.google.com'

# django-allauth
# https://docs.allauth.org/en/latest/installation/quickstart.html
SITE_ID = 1
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    },
}


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Installs
    "debug_toolbar.middleware.DebugToolbarMiddleware"
    # "allauth.account.middleware.AccountMiddleware",  
]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "main.context_processors.base_processors", # actual year
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    # django-allauth
    # 'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = "app.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django_store",
        "USER": "store",
        "PASSWORD": "store",
        "HOST": "localhost",
        "PORT": "5432",
    },
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    # },
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "uk-ua"  # "en-us"
TIME_ZONE = "Europe/Kiev"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

INTERNAL_IPS = [
    "127.0.0.1",
    env.str('INTERNAL_IPS_0', default=''),
    env.str('INTERNAL_IPS_1', default=''),
    env.str('INTERNAL_IPS_2', default=''),
    env.str('INTERNAL_IPS_3', default=''),
    env.str('INTERNAL_IPS_4', default=''),
    env.str('INTERNAL_IPS_5', default=''),
]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": os.path.join(BASE_DIR, "media/cache"),
    }
}

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Override default django values
AUTH_USER_MODEL = 'users.User'
LOGIN_URL = 'user:login'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_PORT = 587
EMAIL_HOST = env.str('EMAIL_HOST', default=''),
EMAIL_HOST_USER = env.str('EMAIL_HOST_USER', default=''),
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD', default=''),

# Кастомні змінні
GOODS_IN_PAGE = 6 # Товарів на сторінці
SITE_NAME = env.str('SITE_NAME', 'Site') # Назва сайту
