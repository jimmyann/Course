import environ
from pathlib import Path

from apps.users import apps

"""
Base settings to build other settings files upon.
"""

ROOT_DIR = environ.Path(__file__) - 3  # (Course/config/settings/base.py - 3 = apps/)
BASE_DIR = Path(__file__).resolve().parent.parent
APPS_DIR = ROOT_DIR.path('apps')  # media, static, staticfiles的文件路径

print(ROOT_DIR)  # /Course
print(BASE_DIR)  # /config
print(APPS_DIR)  # /apps

env = environ.Env()
READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=True)  # 使用.env，此项设置为True
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR.path('.env')))

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', False)
# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'zh-Hans'
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True  # 开启国际化支持
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True  # 使用当前语言环境的格式显示数字和日期
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 提示连接mysql数据库
        'NAME': env.str('DATABASE_NAME'),  # 数据库名为test，要自己创建
        'USER': env.str('DATABASE_USERNAME'),  # 用户名
        'PASSWORD': env.str('DATABASE_PASSWORD'),  # 密码
        'HOST': env.str('DATABASE_HOST'),  # 连接的主机
        'PORT': env.str('DATABASE_PORT'),  # 对应的端口号
    }
}

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
THIRD_PARTY_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
]
LOCAL_APPS = [
    # 第一个apps 代表 目录文件夹， 第二个 apps 表示 users 文件夹下面的apps.py
    'apps.users.apps.UsersConfig',
]
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # django默认的认证
    'allauth.account.auth_backends.AuthenticationBackend',  # django-allauth的认证
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = 'users.User'
# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(APPS_DIR('static'))  # 执行collectstatic命令后会将项目中的静态文件收集到该目录下面来
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'  # 指定静态目录的URL
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [  # 引用位于STATIC_ROOT中的静态文件时使用的网址
    str(APPS_DIR.path('staticfiles')),
]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR('media'))  # 在Windows开发环境下加上.replace("\\", "/")
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
