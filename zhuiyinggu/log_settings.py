"""
logging module settings for zhuiyinggu project.

"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# 设置日志系统
# BASE_LOG_DIR = os.path.join(os.path.dirname(BASE_DIR), "log")
BASE_LOG_DIR = os.path.join(BASE_DIR, "log")

if not os.path.exists(BASE_LOG_DIR):
    os.mkdir(BASE_LOG_DIR)



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # 设置日志格式
    'formatters': {
        # 'verbose': {
        #     'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        # },
        'standard': {
            'format': '[%(asctime)s] [task_id: %(name)s] [process:%(process)d thread:%(threadName)s:%(thread)d] \n'
                      '\t [%(filename)s %(module)s.%(funcName)s:%(lineno)d] [%(pathname)s] \n'
                      '\t [%(levelname)s] ==> %(message)s'
        },
        'simple': {
            'format': '[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s'
        },
        'collect': {
            'fromat': '%(message)s'
        }
    },
    # 设置过滤器
    'filters': {
        # 'special': {
        #     '()': 'project.logging.SpecialFilter',
        #     'foo': 'bar',
        # },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # 设置 handler 对象
    'handlers': {
        # 向屏幕输出，DEBUG 级别 log
        'console': {
            # 'level': 'INFO',
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            # 'formatter': 'simple'
            'formatter': 'standard'
        },
        # # 发送邮件，ERROR 级别log
        # 'mail_admins': {
        #     'level': 'ERROR',
        #     'class': 'django.utils.log.AdminEmailHandler',
        #     'filters': ['special']
        # },
        # 向 zhuiyinggu.log 文件输出，DEBUG 级别 log
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_LOG_DIR, "zhuiyinggu.log"),
            'maxBytes': 1024 * 1024 * 50,  # 日志文件大小 50M
            'backupCount': 100,  # 备份份数
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        # 向 error.log 文件输出，ERROR 级别 log
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_LOG_DIR, "error.log"),
            'maxBytes': 1024 * 1024 * 50,  # 日志文件大小 50M
            'backupCount': 10,
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        # 向 collect.log 文件输出，INFO 级别 log
        'collect': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_LOG_DIR, "collect.log"),
            'maxBytes': 1024 * 1024 * 50,  # 日志文件大小 50M
            'backupCount': 10,
            'formatter': 'collect',
            'encoding': 'utf-8',
        }
    },
    # 设置 logger 对象
    'loggers': {
        # 在 django 层次结构中捕获全部消息的 logger
        'django': {
            'handlers': ['console', 'default'],
            'propagate': True,
        },
        # 记录与处理请求相关的消息
        'django.request': {
            # 'handlers': ['mail_admins'],
            'handlers': ['console', 'default'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'myproject.custom': {
            # 'handlers': ['console', 'mail_admins'],
            'handlers': ['console', 'default'],
            'level': 'DEBUG',
            # 'filters': ['special']
        },
        'default': {
            'handlers': ['default', 'console', 'error'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'collect': {
            'handlers': ['console', 'collect'],
            'level': 'INFO',
        }
    }
}

"""
# views.py 文件中使用示例
import logging

logger = logging.getLogger('sourceDns.webdns.views')    #刚才在setting.py中配置的logger

try:
    mysql= connectMysql('127.0.0.1', '3306', 'david')
except Exception,e:
            logger.error(e)        #直接将错误写入到日志文件
"""