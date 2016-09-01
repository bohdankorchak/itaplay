"""
Django settings for itaplay project.

Generated by 'django-admin startproject' using Django 1.9.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Settings for sending e-mail
EMAIL_SETTINGS = {'DEFAULT_FROM_EMAIL': 'team@blabla.com',
                  'SERVER_EMAIL': 'someroot@localhost',
                  'EMAIL_HOST': 'smtp.sendgrid.com',
                  'EMAIL_MAIN': 'support@blabla.com',
                  'EMAIL_HOST_USER': 'marcosss',
                  'EMAIL_HOST_PASSWORD': 're$RA8uf',
                  'EMAIL_PORT': 587,
                  'EMAIL_USE_TLS': True,
                  'URL_REGISTRATION': "http://127.0.0.1:8000/auth/register?code="}


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3(lia#l&u8vb%1^-=m8ftvs+&14gp*pm3@%u4bygx_ryw%aq8('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'itaplay',
    'authentication',
    'utils',
    'company',
    'home',
    'clips',
    'player',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]

ROOT_URLCONF = 'itaplay.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.static',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'itaplay.wsgi.application'

LOGIN_URL = '/auth/login/'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'test_database', 
        'USER': 'roman',
        'PASSWORD': 'ro135rj',
        'HOST': 'localhost',
        'PORT': ''
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# E-mail settings

DEFAULT_FROM_EMAIL = EMAIL_SETTINGS['DEFAULT_FROM_EMAIL']
SERVER_EMAIL = EMAIL_SETTINGS['SERVER_EMAIL']
EMAIL_HOST = EMAIL_SETTINGS['EMAIL_HOST']
EMAIL_MAIN = EMAIL_SETTINGS['EMAIL_MAIN']
EMAIL_HOST_USER = EMAIL_SETTINGS['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = EMAIL_SETTINGS['EMAIL_HOST_PASSWORD']
EMAIL_PORT = EMAIL_SETTINGS['EMAIL_PORT']
EMAIL_USE_TLS = EMAIL_SETTINGS['EMAIL_USE_TLS']

try:
    from local_settings import *
except ImportError:
    pass
