
from pathlib import Path
import os, json
from django.conf import settings

from dotenv import load_dotenv
load_dotenv() 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1',".vercel.app", ".now.sh"]

#to allow Django and the Django channel to connect with one another via a message broker

ASGI_APPLICATION = "Messeger.asgi.application" #Messeger.asgi will handle the ASGI
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}
# Application definition

INSTALLED_APPS = [
    "daphne",
    'channels',
    'channels_redis',
    'Chat',
    "whitenoise.runserver_nostatic"
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
    'django.middleware.clickjacking.XFrameOptionsMiddleware'

]

ROOT_URLCONF = 'Messeger.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'dist')],
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

ASGI_APPLICATION = "Messeger.asgi.application"
WSGI_APPLICATION = 'Messeger.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
}
VITE_APP_DIR = os.path.join(BASE_DIR,'dist')
def load_json_from_dist(json_filename="manifest.json"):
    manifest_file_path = Path(str(settings.VITE_APP_DIR), "dist", json_filename)
    if not manifest_file_path.exists():
        raise OSError(
            f"Vite manifest file not found on path: {str(manifest_file_path)}"
        )
    with open(manifest_file_path, "r") as manifest_file:
        try:
            manifest = json.load(manifest_file)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(
                f"Vite manifest file invalid. Maybe your {str(manifest_file_path)} file is empty?"
            ) from e
        else:
            return manifest

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'dist/assets'),
    os.path.join(BASE_DIR, "static"),
]

#STAIC_ROOT = os.path.join(BASE_DIR,'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


