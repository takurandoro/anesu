import os
import sys
import dj_database_url
from pathlib import Path
from dotenv import load_dotenv

# Allow Django to use the same DB connection across multiple threads (optional)
import django.db.backends.utils
django.db.backends.utils.allow_thread_sharing = False

load_dotenv()  # Load environment variables from .env if present

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'default-secret-key')
DEBUG = True  # Change to False in production

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'summative-green-academy-api-final-phase.onrender.com',
]

# Add this explicitly to avoid "ROOT_URLCONF not found" errors
ROOT_URLCONF = 'green_academy.urls'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',
    'corsheaders',
    'whitenoise.runserver_nostatic',

    # Local apps
    'users',
    'courses',
    'enrollments',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Templates (useful if you serve any HTML)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR / 'templates')],  # adjust if needed
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

WSGI_APPLICATION = 'green_academy.wsgi.application'

# Database
DATABASES = {}
if 'test' in sys.argv:
    # Use a separate test DB
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test_greenacademy',
        'USER': 'postgres',
        'PASSWORD': 'password',  # replace with your real password
        'HOST': 'localhost',
        'PORT': '5432',
        'TEST': {
            'NAME': 'test_greenacademy',
        }
    }
else:
    # Main DB (example with Postgres)
    DATABASES['default'] = dj_database_url.config(
        default='postgres://admin:password@localhost:5432/greenacademy'
    )

DATABASES['default']['OPTIONS'] = {
    'connect_timeout': 10,
    # 'sslmode': 'require',  # or 'disable', depending on your setup
}

# Static / Media
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Security (adjust for production)
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# DRF Config
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# CORS
CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "").split(",") if os.getenv("CORS_ALLOWED_ORIGINS") else [
    "http://localhost:3000",
    "https://yourfrontend.com"
]

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': os.getenv('LOGGING_LEVEL', 'ERROR'),
            'propagate': True,
        },
    },
}

# Swagger
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': None,
    'USE_SESSION_AUTH': False,
}

# For running tests
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
DATABASES['default']['TEST'] = {
    'NAME': 'test_greenacademy',
    'SERIALIZE': False,
}

# In green_academy/settings.py
AUTH_USER_MODEL = 'users.User'
