from .base import *
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# SECRET_KEY = env("DJANGO_SECRET_KEY", default="$e%u^o6b!t27319!295+vp#guf5)mtn6p5iz2rxj7(bzvv13l%")
SECRET_KEY = '$e%u^o6b!t27319!295+vp#guf5)mtn6p5iz2rxj7(bzvv13l%'
# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = "django.test.runner.DiscoverRunner"
