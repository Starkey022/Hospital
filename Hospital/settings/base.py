"""
Django settings for Hospital project.

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
SECRET_KEY = 'ke@-3m(n2%gu)&296_3eyw0wegx%z_m!e@b5js!$0gb87+&3ut'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    #Paquete para la autenticacion de usuarios
    'django.contrib.auth',
    #Modulo que asocia los permisos
    'django.contrib.contenttypes',
    #Modulo que se encarga de las sesiones
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Agregamos la app que creamos y con la que trabajaremos
    'administracion',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    #Gestiona sesiones
    'django.contrib.sessions.middleware.SessionMiddleware',
    #Asocia a los usuarios con solicitudes mediante sesiones
    'django.middleware.common.CommonMiddleware',
    #Paquete para utilizar la proteccion contra CSRF (Cross Site Request Forgery)
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Hospital.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            #os.path.join(BASE_DIR, 'templates')
            'templates'
        ],
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

WSGI_APPLICATION = 'Hospital.wsgi.application'


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

#Establecemos el lengujar predeterminado
LANGUAGE_CODE = 'es-mx'

#Establecemos la zona horaria
TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

#Directorio para el uso de los archivos estaticos
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)

#Establecemos a done se redirigiran los usuarios al iniciar sesion
LOGIN_REDIRECT_URL = '/'