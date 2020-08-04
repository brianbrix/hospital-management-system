"""
Django settings for hms project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gu7zfi600631jgv7d8et1a625=7mr7)%o(uay2c05-7lwkdia^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.214.79']

# Application definition

INSTALLED_APPS = [
    'hospital_management_system.apps.HospitalManagementSystemConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework'
]
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'hospital_management_system/statics'),
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

ROOT_URLCONF = 'hms.urls'
REST_FRAMEWORK = {
  'DEFAULT_AUTHENTICATION_CLASSES': (
        'hospital_management_system.backends.JWTUserAuthentication',
        'hospital_management_system.backends.JWTDoctorAuthentication',
  )
}

# AUTHENTICATION_BACKENDS = ['hospital_management_system.backends.DoctorBackend']
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
TEMPLATE_CONTEXT_PROCESSORS = [
    'django.core.context_processors.request',
]

WSGI_APPLICATION = 'hms.wsgi.application'

# Database https://docs.djangoproject.com/en/3.0/ref/settings/#databases sudo /etc/init.d/apache2 stop python3
# manage.py inspectdb > hospital_management_system/models.py-- this is a command to use alraedy existing(legacy)
# databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hospital_management_system',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
        'OPTIONS':
            {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
            }
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
AUTH_USER_MODEL = 'hospital_management_system.Users'
# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
SESSION_COOKIE_SECURE = False
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
