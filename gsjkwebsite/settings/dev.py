from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qv+f8z^w#ixtf!$b0&53zl0$%caf2shamv_0fq3m*6t0tj)5=*'


# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.263.net'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'web@gsjkjt.com'
EMAIL_HOST_PASSWORD = 'gsjkjt123'
DEFAULT_FROM_EMAIL = 'web@gsjkjt.com'

# Simple captcha settings
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
CAPTCHA_FOREGROUND_COLOR = '#00589E'


try:
    from .local import *
except ImportError:
    pass
