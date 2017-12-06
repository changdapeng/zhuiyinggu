"""
accounts/urls.py  URL: /accounts/...

提供基于 User 的: 
GET（查看单个用户、激活用户(URL:/accounts/users/<pk>/active_user/)） 
LIST（查看用户列表）
POST（增加用户）
PUT（更新用户）
DELETE（注销用户） 

提供基于 SystemUserProfile 的: 
GET（查看单个用户、激活用户(URL:/accounts/systemuserprofile/<nickname>/active_user/)） 
LIST（查看用户列表） 
POST（增加用户） 
PUT（更新用户） 
DELETE（注销用户） 

提供基于 UserProfile 的: 
GET（查看单个用户、激活用户(URL:/accounts/userprofile/<nickname>/active_user/)） 
LIST（查看用户列表） 
POST（增加用户） 
PUT（更新用户） 
DELETE（注销用户） 

提供基于 Token 的: 
POST（获取token） 
"""
from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from accounts import views



router = DefaultRouter()
router.register(r'users', views.UserViewSet, base_name='user')
router.register(r'systemuserprofile', views.SystemUserProfileViewSet)
router.register(r'userprofile', views.UserProfileViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),

    # url()函数传递四个参数，两个必选参数：regex和view，两个可选参数：kwargs和name。
    # regex，意思是“正则表达式”，它是用于匹配字符串中的模式的语法，换言之，在这里是匹配url。
    # Django从第一个正则表达式开始，在列表中自上而下匹配，将请求的URL与每个正则表达式进行比较，直到找到匹配的一个。
    # 这些正则表达式是第一次加载URLconf模块时被编译。 它们超级快，只要查找不是太复杂。
    # view，当Django发现正则表达式匹配时，Django将调用指定的视图函数，使用HttpRequest对象作为第一个参数，
    # 并将正则表达式中的任何“捕获”值作为其他参数。如果正则表达式使用简单的捕获，则值作为位置参数传递；
    # 如果它使用命名捕获，则值作为关键字参数传递。
    # kwargs，任意关键词参数可以在字典中传递到目标视图。
    # name，命名你的URL可让你从Django其他地方明确地引用它，特别是在模板中。
    url(r'^gettoken/$', views.GetToken.as_view()),
]



