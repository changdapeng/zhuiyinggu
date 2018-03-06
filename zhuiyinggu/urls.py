"""zhuiyinggu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
# from rest_framework.authtoken import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('accounts.urls')),
    url(r'^data/', include('data_manage.urls')),
    url(r'^apk/', include('apk_manage.urls')),
    url(r'^blog/', include('blog.urls')),
    
    # REST Framework 的登陆和注销视图URL
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^api-token-auth/', views.obtain_auth_token),
    # social-app-django 认证
    # url('', include('social_django.urls', namespace='social')),

]


# import debug_toolbar
urlpatterns = [
 #       url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
