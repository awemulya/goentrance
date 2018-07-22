from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'go',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        }
}

INSTALLED_APPS += [

    'debug_toolbar',

]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',

]
INTERNAL_IPS = '127.0.0.1'

LOGIN_REDIRECT_URL = '/core/'

# STATICFILES_DIRS = [
#         os.path.join(BASE_DIR, "static")
#     ]
#
# STATIC_ROOT = os.path.join(BASE_DIR, 'a-static')


# WEBPACK_LOADER = {
#     'DEFAULT': {
#         'CACHE': False,
#         # 'BUNDLE_DIR_NAME': '/dist/',#('/build/' if DEBUG else '/dist/'),
#         'BUNDLE_DIR_NAME': '/build/',#('/build/' if DEBUG else '/dist/'),
#         # 'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
#         'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats-local.json'),
#     }
# }
