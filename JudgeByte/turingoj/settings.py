"""
Django settings for turingoj project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR_turingoj = os.path.join(BASE_DIR, "turingoj/templates")
TEMPLATE_DIR_coders = os.path.join(BASE_DIR, "coders/templates")
TEMPLATE_DIR_problems = os.path.join(BASE_DIR, "problems/templates")
TEMPLATE_DIR_submissions = os.path.join(BASE_DIR, "submissions/templates")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# DB_NAME = 'turingojdb'  # Database Name
# DB_USER = 'turingojuser'  # Database User
# DB_HOST = 'localhost'  # Database Server
# DB_PORT = ''  # Database Server Port

SECRET_KEY = '+ujkp)r1q)%4sj)&9&v3&qlqr#&r@x8b3pznzl54x9$me*k7zp'

# with open('/etc/turingojdb_pass.txt') as f:
#     DB_PASS = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['192.168.1.101', '127.0.0.1', '192.168.159.86']
ALLOWED_HOSTS = [ '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    # for applying migrations first comment this and apply migration to the coders app and then uncomment and migrate
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'private_storage',  # for serving files privately
    'coders',
    'problems',
    'submissions',
    'django_extensions',
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

ROOT_URLCONF = 'turingoj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR_turingoj, TEMPLATE_DIR_coders, TEMPLATE_DIR_problems, TEMPLATE_DIR_submissions],
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

WSGI_APPLICATION = 'turingoj.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'judgedb',
        'USER': 'root',
        'PASSWORD': 'mitra1341',
        'HOST': '127.0.0.1',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'coders.UserProfile'  # Adding this line for abstractuser model
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'turingoj/static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticroot')
LOGIN_REDIRECT_URL = 'homepage'
LOGOUT_REDIRECT_URL = 'homepage'

PRIVATE_STORAGE_ROOT = os.path.join(BASE_DIR, 'turingoj/private_media')
PRIVATE_STORAGE_AUTH_FUNCTION = 'private_storage.permissions.allow_superuser'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'