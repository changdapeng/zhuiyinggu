from django.conf.urls import url, include

from rest_framework import renderers
from rest_framework.routers import DefaultRouter

from blog import views



router = DefaultRouter()
router.register(r'tag', views.TagViewSet, base_name='tag')
router.register(r'blog', views.BlogViewSet, base_name='blog')


urlpatterns = [
    url(r'^', include(router.urls)),
]