import os, sys
from configurations import Configuration
from django.utils import translation
from django.utils.translation import gettext_lazy as _
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from datetime import timedelta


class Base(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = '=hky*vk78kz$7cw7@t$*-&elahkz+!gc&qfs2f17ry+o-blh)@'

    # SECURITY WARNING: don't run with debug turned on in production!

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'django_cron',
        'rest_framework',
        'rest_framework.authtoken',
        'djoser',
        'drf_yasg',
    ]

    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.authentication.TokenAuthentication',
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ],
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE': 100,
    }

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'app.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'app.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/3.0/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('POSTGRES_DB'),
            'USER': os.getenv('POSTGRES_USER'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
            'HOST': os.getenv('POSTGRES_SERVER'),
        }
    }

    # Password validation
    # https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

    # Internationalization
    # https://docs.djangoproject.com/en/3.0/topics/i18n/

    LANGUAGE_CODE = 'en-US'

    LANGUAGES = [
        ('uk-UA', _('Ukrainian')),
        ('ru-RU', _('Russian')),
        ('en-US', _('English'))
    ]

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.0/howto/static-files/

    STATIC_URL = '/static/'

    DJOSER = {
        'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
        'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
        'ACTIVATION_URL': '#/activate/{uid}/{token}',
        'SEND_ACTIVATION_EMAIL': False,
        'SERIALIZERS': {},
    }

    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
        'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
        'ROTATE_REFRESH_TOKENS': False,
        'BLACKLIST_AFTER_ROTATION': True,

        'ALGORITHM': 'HS256',
        'SIGNING_KEY': SECRET_KEY,
        'VERIFYING_KEY': None,
        'AUDIENCE': None,
        'ISSUER': None,

        'AUTH_HEADER_TYPES': ('JWT',),
        'USER_ID_FIELD': 'id',
        'USER_ID_CLAIM': 'user_id',

        'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
        'TOKEN_TYPE_CLAIM': 'token_type',

        'JTI_CLAIM': 'jti',

        'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
        'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
        'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
    }

    AUTH_USER_MODEL = 'user.User'



    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    # SMTP
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = os.getenv('SMTP_HOST')
    EMAIL_HOST_USER = os.getenv('SMTP_USER')
    EMAIL_HOST_PASSWORD = os.getenv('SMTP_PASSWORD')
    EMAIL_PORT = os.getenv('SMTP_PORT')
    EMAIL_USE_SSL = os.getenv('SMTP_TLS')
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


class Dev(Base):
    DEBUG = True

    ALLOWED_HOSTS = [
        'backend',
        'localhost',
    ]


class Prod(Base):
    DEBUG = False

    ALLOWED_HOSTS = ['*']
