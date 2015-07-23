

"""
Django settings for user_a project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from mongoengine import connect,ConnectionError
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.join(BASE_DIR,os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)
DBNAME =  os.environ.get("DBNAME") 
MONGO_DATABASE_NAME = DBNAME
print DBNAME
MONGO_PORT_27017_TCP_ADDR = os.environ.get("MONGO_PORT_27017_TCP_ADDR","127.0.0.1")
MONGO_PORT_27017_TCP_PORT = int(os.environ.get("MONGO_PORT_27017_TCP_PORT","27017"))
DB = connect(DBNAME,host=MONGO_PORT_27017_TCP_ADDR, port=MONGO_PORT_27017_TCP_PORT)

DOMAIN = os.environ.get("DOMAIN")
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#pbp1-t0jx50zbunfsptyi+=l61)bc8==0kunk&#!hv3=n373t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_user_agents',
    'mongoengine.django.mongo_auth',
)

# Cache backend is optional, but recommended to speed up user agent parsing
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Name of cache backend to cache user agents. If it not specified default
# cache alias will be used. Set to `None` to disable caching.
USER_AGENTS_CACHE = 'default'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
MONGOENGINE_USER_DOCUMENT = 'web.user.participant.models.Participant'
SOCIAL_AUTH_USER_MODEL = 'web.user.participant.models.Participant'
AUTH_USER_MODEL = 'mongo_auth.MongoUser'
AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    # 'mongoengine.django.auth.MongoEngineBackend',
    'web.auth_backends.NonSocialUserAuth',
)

ROOT_URLCONF = 'user_a.urls'

WSGI_APPLICATION = 'user_a.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',
    }
}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
SESSION_ENGINE = 'mongoengine.django.sessions'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'GMT'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
