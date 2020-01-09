from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS = INSTALLED_APPS + [
    'wagtail.contrib.styleguide',
    'wagtaillinkchecker',
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'banana'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'webpage_db',
#         'USER': 'webpage_manager_1',
#         'PASSWORD': 'supersecurepassword123',
#         'HOST': 'db',
#         'PORT': 5432
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

'''
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'webpage.my.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'MYAPP': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}
'''

# captch Settings
RECAPTCHA_PUBLIC_KEY = 'banana'
RECAPTCHA_PRIVATE_KEY = 'banana'
NOCAPTCHA = True

# wagtailmaps settings
# Mandatory
WAGTAIL_ADDRESS_MAP_CENTER = 'London, UK'  # It must be a properly formatted address
WAGTAIL_ADDRESS_MAP_KEY = 'banana'

try:
    from .local import *
except ImportError:
    pass
