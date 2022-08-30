"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import django
import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


import os
from django.core.exceptions import ImproperlyConfigured

# def get_env_variable(var_name):
#     try:
#         return os.environ[var_name]
#     except KeyError:
#         error_msg = "Set the %s environment variable" % var_name
#         raise ImproperlyConfigured(error_msg)

# SECRET_KEY = get_env_variable('SECRET_KEY')

# from django.utils.crypto import get_random_string
# chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
# SECRET_KEY = get_random_string(50, chars)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f(clfjc_*^5%&jx3_6d7$ac=4m&*msx^@t=9qkuv@3#dx_i+sr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']



SITE_ID = 1
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'myapp.apps.MyappConfig',
    'django_celery_beat',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

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

import os

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
        
#     }
# }


DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'd24n5gsrjmp9kl',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'qeczfcfgeyugic',
        'PASSWORD': '6ef3098a8499da9e38253fc0391a2e758359f2e8b07917f96028e4ab0c6920c5',
        'HOST': 'ec2-3-225-110-188.compute-1.amazonaws.com',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',                      # Set to empty string for default.
    }
}

CELERY_IMPORTS = (
    'myapp.tasks',
)

# import dj_database_url
# # #
# DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# DATABASES['default'] =  dj_database_url.config()

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'Asia/Kolkata' 

USE_I18N = True

USE_L10N = True

USE_TZ = False

# CELERY_BROKER_URL = 'amqp://localhost'
CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'
# BROKER_URL = 'django://'
#CELERY_BROKER_URL = 'redis://:p1b6b84e67facd107957e878035c0fc2ad3da5f6d4ca0c138e7bac0f4a3bfb055@ec2-54-152-181-10.compute-1.amazonaws.com:27179'
#CELERY_RESULT_BACKEND = 'redis://:p1b6b84e67facd107957e878035c0fc2ad3da5f6d4ca0c138e7bac0f4a3bfb055@ec2-54-152-181-10.compute-1.amazonaws.com:27179'
# Static files (CSS, JavaScript, Images)
# Celery Configuration Options
# CELERY_TIMEZONE = "Asia/kol"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'myapp/static')
]


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()