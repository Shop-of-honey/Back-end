import os

from settings import BASE_DIR

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/staticfiles/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles'),
)
