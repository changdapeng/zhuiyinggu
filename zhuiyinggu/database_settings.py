"""
database module settings for zhuiyinggu project.

"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# 使用sqlite3数据库
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

# 使用MySQL数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'init_command': 'SET storage_engine=INNODB',
        'OPTIONS': {
            'read_default_file': '/home/zyg/zhuiyinggu/zhuiyinggu/my.conf',
        },
    }
}

# 可能会用到的配置
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         # "LOCATION": "redis://r-2ze8fb1b0e246864.redis.rds.aliyuncs.com:6379",
#         "LOCATION": "redis://127.0.0.1:6379",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             # "PASSWORD": "3531368cdda7R",
#         }
#     }
#
# }

#
# }