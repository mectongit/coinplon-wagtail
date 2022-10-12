from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-d_0)719h+06g=!wi^(lm#dis#t!ao0in!qqpc+o=)p9%v+=h)%"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = ["django.core.mail.backends.console.EmailBackend"]

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware",] + MIDDLEWARE

INTERNAL_IPS = ["127.0.0.1"]

try:
    from .local import *
except ImportError:
    pass
