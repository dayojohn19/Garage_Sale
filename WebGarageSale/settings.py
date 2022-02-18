"""
Django settings for WebGarageSale project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import pymongo
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r@0q-usq-)ms88-2ooq+yju-r*_b3)w8fq+8dmasf2pmolss3j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*', '0.0.0.0']


# Application definition

INSTALLED_APPS = [
    'AppUsers',
    'ApplicationGarage',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'WebGarageSale.urls'

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

WSGI_APPLICATION = 'WebGarageSale.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# *********************---Default-----*********************
# *********************---Default-----*********************
# *********************---Default-----*********************
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# *********************---ASIA-----*********************
# *********************---ASIA-----*********************
# *********************---ASIA-----*********************

# client = pymongo.MongoClient(
#     "mongodb+srv://jc:jc@cluster2.wk77x.mongodb.net/21?retryWrites=true&w=majority")
# db = client.test

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': '21',
#         # 'ENFORCE_SCHEMA': False,
#         'CLIENT': {
#             'host': 'mongodb+srv://jc:jc@cluster2.wk77x.mongodb.net/21?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE'
#         }
#     }
# }
# 'mongodb+srv://jc:jc@cluster2.wk77x.mongodb.net/21?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE'
#
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Manila'
TIME_INPUT_FORMATS = ('%I:%M %p',)

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'images')
# MEDIA_URL = '/images/'
if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    MEDIA_URL = '/images/'

else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATIC_URL = '/static/'

MEDIA_ROOT = [os.path.join(BASE_DIR, 'images')]
# MEDIA_URL = '*/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'images/')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'ApplicationGarage/static')
]
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
