# REST Framework 相关设置
# 其设置 全为 “全局设置”
# -----------------------
REST_FRAMEWORK = {

    #设置认证方式 为 rest 的token认证
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 可能会用到的配置
        #'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        #'rest_framework_social_oauth2.authentication.SocialAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),

    #可能会用到的配置
    #'DEFAULT_PERMISSION_CLASSES':(
    #      'rest_framework.permissions.IsAuthenticated',
    # )
    # 序列化时展示的时间个格式
    # 'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S",
    # 自定义返回值，修改默认只有detail的返回值
    # 'EXCEPTION_HANDLER': 'web.utils.custom_exception_handler.custom_exception_handler',
    # 注册用户是的密码错误
    # 'NON_FILELD_ERRORS_KEY': "password",
    # 使用Django rest framework api时，客户端返回结果为html标签，将结果返回json
    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    # ),


    # # 设置过滤器 为 rest 的过滤器
    # 'DEFAULT_FILTER_BACKENDS': (
    #     'django_filters.rest_framework.DjangoFilterBackend',
    # ),


    # 设置按用户和匿名用户限流
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '1000/day',
        'user': '100/day',
    },


    # 增加分页
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,


    # 设置按作用域限流
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.ScopedRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'user': '1000/day',
        'systemuserprofile': '1000/day',
        'userprofile': '1000/day',
    }

}