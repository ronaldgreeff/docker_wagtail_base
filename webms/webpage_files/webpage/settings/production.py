from .base import *
from decouple import config, Csv
from datetime import timedelta

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS = INSTALLED_APPS + [
    'wagtail.contrib.styleguide',
    'wagtailcache',
    'axes',
    'sendgrid',
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}

AUTHENTICATION_BACKENDS = [
    # AxesBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesBackend',
    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]

MIDDLEWARE = ['wagtailcache.cache.UpdateCacheMiddleware',] + MIDDLEWARE + [
        'axes.middleware.AxesMiddleware',
        'csp.middleware.CSPMiddleware',
        'wagtailcache.cache.FetchFromCacheMiddleware',
    ]

try:
    from .local import *
except ImportError:
    pass

CACHES = {
    'default': {
        'BACKEND': 'wagtailcache.compat_backends.django_redis.RedisCache',
        'LOCATION': 'redis://redis:6379/webpage_db',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
        'KEY_PREFIX': 'wagtailcache',
        'TIMEOUT': 86400, # expire in a day
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'https://example-company.uksouth.cloudapp.azure.com:80'


# captch Settings
RECAPTCHA_PUBLIC_KEY = config('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = config('RECAPTCHA_PRIVATE_KEY')
NOCAPTCHA = True

# wagtailmaps settings
# Mandatory
WAGTAIL_ADDRESS_MAP_CENTER = 'London, UK'  # It must be a properly formatted address
WAGTAIL_ADDRESS_MAP_KEY = config('WAGTAIL_ADDRESS_MAP_KEY')

# Static Files
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# HTTPS secure
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True

# to be notified by an email on a 500 response
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
    ('example-company', 'devops@example-company.org.uk'),
)

# SECURE_PROXY_SSL_HEADER = ['HTTP_X_FORWARDED_PROTO', 'https']

# Email configuration
EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
SERVER_EMAIL='devops@example-company.org.uk'

# CSP policy
CSP_REPORT_ONLY = True
# CSP_EXCLUDE_URL_PREFIXES = ('public.tableau.com',)
CSP_DEFAULT_SRC = ["'self'", ]
# CSP_SCRIPT_SRC = ["'self'", 'public.tableau.com',]
# CSP_IMG_SRC =
# CSP_OBJECT_SRC =
# CSP_MEDIA_SRC =
CSP_FRAME_SRC = None
# CSP_FONT_SRC =
# CSP_CONNECT_SRC =
# CSP_STYLE_SRC =
# CSP_BASE_URI =
# CSP_FRAME_ANCESTORS =
# CSP_FORM_ACTION =
# CSP_SANDBOX =
# CSP_REPORT_URI =
# CSP_MANIFEST_SRC =
# CSP_WORKER_SRC =
# CSP_PLUGIN_TYPES =
# CSP_REQUIRE_SRI_FOR =
# CSP_UPGRADE_INSECURE_REQUESTS =
# CSP_BLOCK_ALL_MIXED_CONTENT =
# CSP_INCLUDE_NONCE_IN =

# Django Axes settings (from the wagtailenforcer)
AXES_FAILURE_LIMIT = 5
AXES_LOCK_OUT_AT_FAILURE = True
AXES_COOLOFF_TIME = timedelta(minutes=10)
AXES_ONLY_USER_FAILURES = False  # Lock out based on username and not IP or UserAgent
AXES_LOCKOUT_TEMPLATE = 'lockout.html'
AXES_RESET_ON_SUCCESS = True

# Axes reverse proxy configuration
AXES_PROXY_COUNT = 1

# Axes configuration handler
AXES_HANDLER = 'axes.handlers.database.AxesDatabaseHandler'
