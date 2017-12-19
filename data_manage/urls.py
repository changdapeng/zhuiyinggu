"""
data_manage/urls.py  URL: /data_manage/...

提供基于 Game、Movie、Music、Book、Video 的: 
GET（查看单个模型对象、查看最新模型对象(URL:/apk/apk_version/newest/)） 
LIST（查看模型对象列表）
POST（增加模型对象）
PUT（更新模型对象）
DELETE（注销模型对象）
"""
from django.conf.urls import url, include

from rest_framework import renderers
from rest_framework.routers import DefaultRouter

from data_manage import views

router = DefaultRouter()
  
router.register(r'Game', views.GameViewSet)
router.register(r'Movie', views.MovieViewSet)
router.register(r'Music', views.MusicViewSet)
router.register(r'Book', views.BookViewSet)
router.register(r'Video', views.VideoViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    
    ]

