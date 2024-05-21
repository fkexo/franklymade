"""
Django settings for franklymade project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

load_dotenv()





# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.getenv('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = os.environ.get('DEBUG', 'from_env') == "True"

print(DEBUG)
ALLOWED_HOSTS = ['franklymade-nncs.onrender.com', 'localhost',  'http://127.0.0.1:8000']


# Application definition

INSTALLED_APPS = [
    
    'accounts',
    'tech',
    'blog',
    'tutorial',
    'portinfo',
    
    'ckeditor',
    
    'crispy_forms',
    'crispy_bootstrap5',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'trumbowyg',

]


CKEDITOR_UPLOAD_PATH = 'content/ckeditor/'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',


    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# i added this message storage for the messages
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
# MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

ROOT_URLCONF = 'franklymade.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'franklymade/templates'),
            os.path.join(BASE_DIR, 'portinfo/templates'),
            os.path.join(BASE_DIR, 'portinfo/templates/portinfo'),
            os.path.join(BASE_DIR, 'tech/templates'),
           
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

WSGI_APPLICATION = 'franklymade.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'website-postgresql-franklymade',
    'USER': USER,
    'PASSWORD': PASSWORD, # Replace with the actual password
    'HOST': 'dpg-cp2eom21hbls739g011g-a',
    'PORT': '5432',
    }

}

DATABASE_URL = os.getenv('DATABASE_URL ')

# this will enable database update from development environmet
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)



STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
}
# DATABASES = {
#     'default': dj_database_url.parse(os.getenv('DATABASE_URL'))
#     }



# Password validation
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



# this will log bug to console even when debug is set to False.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    # 'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            #'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            #'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}

# this for code syntax highlighting for python javaScript, HTML CSS
CKEDITOR_PLUGINS = [
    # ...
    'codesnippet',
    # ...
]




CKEDITOR_CONFIGS = {
    'default': {
        # ...
        'codemirror': {
            'theme': 'material',
            'modes': ['python', 'javascript', 'html', 'css'],
            'lineNumbers': True,
            'lineWrapping': True,
        },
        # ...
    }
}

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# for email smtp
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
# EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = 'frankmadu2live@gmail.com'
EMAIL_HOST_PASSWORD = 'bhtm tcvp cbis hbja'



# for the tinymce configuration


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
# i am using this whitenoise to server media files in production when debug = False
WHITENOISE_MEDIA_PREFIX = '/media/'
WHITENOISE_MAX_AGE = 31536000  # 1 year


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# lets tell django where to look for static files in our project folder
STATICFILES_DIRS =[ os.path.join(
    BASE_DIR, 'franklymade/static',
    ),
]



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'd5j8gbnfmt7lv8',
#         'USER': '{}'.format(database_USER),
#         'PASSWORD': '{}'.format(database_PASSWORD),
#         'HOST': 'ec2-3-212-90-231.compute-1.amazonaws.com'
#     }
# }



# db_from_env = dj_database_url.config()
# DATABASES['default'].update(db_from_env)



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
