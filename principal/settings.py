from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h5)1hfx3qxizlp53yt-_=04pfhu!vjlo9n98(b4()og*55n@86'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
X_FRAME_OPTIONS = 'ALLOWALL'

# Application definition
INSTALLED_APPS = [
    
    'partidas_planos',
    'centro_costos',
    'control_expediente',
    'hoja_requerimiento',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'principal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'principal.wsgi.application'

# Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# PATH FILES
MEDIA_ROOT = r'\\Pc-03\d\Partidas y Planos 2024 - 2025\SDI'
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'SDI_dev',
        'USER': 'Admin',
        'PASSWORD': 'root',
        'HOST': r'PC-03\SQLEXPRESS',
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',  # asegúrate de tener este instalado
            'extra_params': 'TrustServerCertificate=yes;',  # útil para evitar errores SSL
        },
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'mssql',
#         'NAME': 'SDI_dev',
#         'USER': 'sa',
#         'PASSWORD': 'sa',
#         'HOST': r' 192.168.100.108',
#         'PORT': '1433',  # por defecto es 1433
#         'OPTIONS': {
#             'driver': 'ODBC Driver 17 for SQL Server',  # asegúrate de tener este instalado
#             'extra_params': 'TrustServerCertificate=yes;',  # útil para evitar errores SSL
#         },
#     }
# }

# Password validation
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
LANGUAGE_CODE = 'en'
#TIME_ZONE = 'UTC'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = False

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    'static'
]
# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# USER CUSTOMIZE
AUTH_USER_MODEL = 'partidas_planos.User'
LOGIN_URL = '/login/' 

SECURE_CROSS_ORIGIN_OPENER_POLICY = None
SECURE_CROSS_ORIGIN_EMBEDDER_POLICY = None
