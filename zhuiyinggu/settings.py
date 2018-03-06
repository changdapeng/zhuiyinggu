"""
Django settings for zhuiyinggu project.

Generated by 'django-admin startproject' using Django 1.11.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8148n1#iw@eqdfj7@$uh^o8+ha&6tzb*6uz&240001b+d!pai('

# SECURITY WARNING: don't run with debug turned on in production!
# 仅当 DEBUG 设置为True时才启用日志记录
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ['*',]


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # REST Framework 
    'guardian',  # guardian 认证模块
    'rest_framework.authtoken',  # DRF token 认证
    'django_filters',  # django-filter 过滤器插件
    'crispy_forms', # 提高DRF(Django REST Framework)过滤器在网页上的的可视化模块
    #'debug_toolbar',  # django-debug-toolbar
    # 'social_django',  # social-app-django
    'accounts.apps.AccountsConfig',  # 自定义用户、用户管理
    'data_manage.apps.DataManageConfig',  #  数据、资料管理
    'apk_manage.apps.ApkManageConfig',  # APP 版本管理
    'blog.apps.BlogConfig',  # Blog 管理

    # 可能会用到的app
    #'oauth2_provider',
    #'social_django',
    #'rest_framework_social_oauth2',
    #'corsheaders',
    ####'kingadmin',
    ####'management',
    ####'mentor',


]

"""
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
"""


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 可能会用到的中间件
    #'corsheaders.middleware.CorsMiddleware',
    #'django.middleware.common.CommonMiddleware',
    #'web.utils.middleware.CustomLoginSessionMiddleware',
]

ROOT_URLCONF = 'zhuiyinggu.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        # 可能用到的配置
        #'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # # social-app-django 配置,可能会用到
                # 'social_django.context_processors.backends',  # for oauth2
                # 'social_django.context_processors.login_redirect',  # for oauth2
            ],
        },
    },
]

WSGI_APPLICATION = 'zhuiyinggu.wsgi.application'





# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',  # 优先使用argon2作为默认存储算法
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'


# 设置为上海的UTC时间
#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# 设置激活或停用对时区的支持
# 修改数据库是MySQL时，配置为False，使得TIME_ZONE的设置生效
#USE_TZ = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT='/data/zhuiyinggu/static'
# 可能会用到的配置
#STATIC_ROOT = os.path.join(BASE_DIR, 'static',)
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
# )

MEDIA_URL = '/media/'
MEDIA_ROOT = '/data/zhuiyinggu/media'




# 可能会用到的配置
#CORS_ORIGIN_ALLOW_ALL = True





# 指定使用自定义的用户模型
AUTH_USER_MODEL = 'accounts.MyUser'

AUTHENTICATION_BACKENDS = (
    # 可能会用到的配置
    # 'rest_framework_social_oauth2.backends.DjangoOAuth2',
    # 'web.view.verify_view.CustomBackend',
    # # #第三方认证登录配置，微博、微信、QQ
    # 'social_core.backends.weibo.WeiboOAuth2',
    # 'social_core.backends.qq.QQOAuth2',
    # 'social_core.backends.weixin.WeixinOAuth',
    'django.contrib.auth.backends.ModelBackend',  # default
    'guardian.backends.ObjectPermissionBackend',
)


# SOCIAL_AUTH_WEIBO_KEY = '23xxxxxxx'  # 微博
# SOCIAL_AUTH_TWITTER_SECRET = '2c60B652xxxxcxxxxxxxxx'  # 微博
#
# SOCIAL_AUTH_QQ_KEY = '0lcx9Vd0R4oVfLan'  # QQ
# SOCIAL_AUTH_QQ_SECRET = '1106683989'  # QQ
#
# SOCIAL_AUTH_WEIXIN_KEY = 'foobar'  # 微信
# SOCIAL_AUTH_WEIXIN_SECRET = 'bazqux'  # 微信
#
# #第三方登录成功后跳转页面,这里跳转的主页
# SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/index/'



# 导入 logging 日志配置
from zhuiyinggu.log_settings  import *

# 导入数据库配置
from zhuiyinggu.database_settings import *

# 导入 REST Framework 配置
from zhuiyinggu.DRF_settings import *




