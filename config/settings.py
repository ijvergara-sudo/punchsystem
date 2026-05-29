
from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-local-development-secret-key')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '.onrender.com',
]
=======
import os
import dj_database_url

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-secret-key'
DEBUG = True
ALLOWED_HOSTS = ['*']
>>>>>>> b673fa0a2f578d336e17974dd3669d014a1c67e7

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'attendance',
]

MIDDLEWARE = [
<<<<<<< HEAD
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
=======
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
>>>>>>> b673fa0a2f578d336e17974dd3669d014a1c67e7
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
<<<<<<< HEAD
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
=======
>>>>>>> b673fa0a2f578d336e17974dd3669d014a1c67e7
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

<<<<<<< HEAD
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
    )
}
=======

>>>>>>> b673fa0a2f578d336e17974dd3669d014a1c67e7

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Puerto_Rico'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
<<<<<<< HEAD
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
=======
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
    )
}
>>>>>>> b673fa0a2f578d336e17974dd3669d014a1c67e7
