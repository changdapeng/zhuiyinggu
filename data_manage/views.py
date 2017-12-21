"""
data_manage/views.py

基于Django框架、guardian框架、REST Framework框架，实现RESTful风格接口。

实现ApkVersion模型的 GET LIST POST PUT DELETE 以及自定义相关功能。

支持 用户认证、权限控制、过滤器、限流器、分页。
"""
from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import filters

from data_manage.permissions import IsSystemUserOrReadOnly, IsAuthenticatedOrReadOnly, ReadOnly
from data_manage.models import Game, Movie, Music, Book, Video
from data_manage.serializers import GameSerializer, MovieSerializer, MusicSerializer, BookSerializer, VideoSerializer

from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend


# Game 过滤器
# -----------
class GameFilter(rest_framework.FilterSet):
    """
    过滤的字段为 name，用于为不同的apk实现不同的接口。
    
    [FieldFilter] URL 格式为： http://www.zhuiyinggu.com:33333/apk/apk_version/?name=Face2Face
    """
    
    class Meta:
        model = Game
        fields = ['name',]


# Game 版本控制
# -------------
class GameViewSet(viewsets.ModelViewSet):
    """
    用于进行 game管理。
    对应 Game 模型，通过过滤器对不同的软件提供不同的接口。
    提供返回某一apk的版本，或者返回某一apk的最新版本。
    只有systemuser可以增加、修改、删除apk版本信息。
    其他普通用户和未登录用户只有查看权限。   
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    #lookup_field = 'name'
     
    permission_classes = (IsAuthenticatedOrReadOnly, IsSystemUserOrReadOnly, )    
    
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    
    filter_class = GameFilter
        
    ordering_fields = ('name',) 
    ordering = ('name',)
    search_fields = ('name',)

    # # 按用户限流
    # throttle_classes = (UserRateThrottle,)
    # # 按作用域限流
    # throttle_scope = 'user'
             
       
    def update(self, request, *args, **kwargs):
        """
        覆写 update()
        设置partial属性为True使其序列化时字段可以部分更新
        """
        partial = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


# Movie 过滤器
# ------------
class MovieFilter(rest_framework.FilterSet):
    """
    过滤的字段为 name，用于为不同的apk实现不同的接口。
    
    [FieldFilter] URL 格式为： http://www.zhuiyinggu.com:33333/apk/apk_version/?name=Face2Face
    """
    
    class Meta:
        model = Movie
        fields = ['name',]


# Movie 版本控制
# --------------
class MovieViewSet(viewsets.ModelViewSet):
    """
    用于进行 game管理。
    对应 Game 模型，通过过滤器对不同的软件提供不同的接口。
    提供返回某一apk的版本，或者返回某一apk的最新版本。
    只有systemuser可以增加、修改、删除apk版本信息。
    其他普通用户和未登录用户只有查看权限。   
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    #lookup_field = 'name'
     
    permission_classes = (IsAuthenticatedOrReadOnly, IsSystemUserOrReadOnly, )    
    
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    
    filter_class = MovieFilter
        
    ordering_fields = ('name',) 
    ordering = ('name',)
    search_fields = ('name',)

    # # 按用户限流
    # throttle_classes = (UserRateThrottle,)
    # # 按作用域限流
    # throttle_scope = 'user'
             
       
    def update(self, request, *args, **kwargs):
        """
        覆写 update()
        设置partial属性为True使其序列化时字段可以部分更新
        """
        partial = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)



# Music 过滤器
# ------------
class MusicFilter(rest_framework.FilterSet):
    """
    过滤的字段为 name，用于为不同的apk实现不同的接口。
    
    [FieldFilter] URL 格式为： http://www.zhuiyinggu.com:33333/apk/apk_version/?name=Face2Face
    """
    
    class Meta:
        model = Music
        fields = ['name',]


# Music 版本控制
# --------------
class MusicViewSet(viewsets.ModelViewSet):
    """
    用于进行 game管理。
    对应 Game 模型，通过过滤器对不同的软件提供不同的接口。
    提供返回某一apk的版本，或者返回某一apk的最新版本。
    只有systemuser可以增加、修改、删除apk版本信息。
    其他普通用户和未登录用户只有查看权限。   
    """
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    #lookup_field = 'name'
     
    permission_classes = (IsAuthenticatedOrReadOnly, IsSystemUserOrReadOnly, )    
    
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    
    filter_class = MusicFilter
        
    ordering_fields = ('name',) 
    ordering = ('name',)
    search_fields = ('name',)

    # # 按用户限流
    # throttle_classes = (UserRateThrottle,)
    # # 按作用域限流
    # throttle_scope = 'user'
             
       
    def update(self, request, *args, **kwargs):
        """
        覆写 update()
        设置partial属性为True使其序列化时字段可以部分更新
        """
        partial = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)



# Book 过滤器
# -----------
class BookFilter(rest_framework.FilterSet):
    """
    过滤的字段为 name，用于为不同的apk实现不同的接口。
    
    [FieldFilter] URL 格式为： http://www.zhuiyinggu.com:33333/apk/apk_version/?name=Face2Face
    """
    
    class Meta:
        model = Book
        fields = ['name',]


# Book 版本控制
# -------------
class BookViewSet(viewsets.ModelViewSet):
    """
    用于进行 Book 管理。
    对应 Book 模型，通过过滤器对不同的软件提供不同的接口。
    提供返回某一apk的版本，或者返回某一apk的最新版本。
    只有systemuser可以增加、修改、删除apk版本信息。
    其他普通用户和未登录用户只有查看权限。   
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #lookup_field = 'name'
     
    permission_classes = (IsAuthenticatedOrReadOnly, IsSystemUserOrReadOnly, )    
    
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    
    filter_class = BookFilter
        
    ordering_fields = ('name',) 
    ordering = ('name',)
    search_fields = ('name',)

    # # 按用户限流
    # throttle_classes = (UserRateThrottle,)
    # # 按作用域限流
    # throttle_scope = 'user'
             
       
    def update(self, request, *args, **kwargs):
        """
        覆写 update()
        设置partial属性为True使其序列化时字段可以部分更新
        """
        partial = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)



# Video 过滤器
# ------------
class VideoFilter(rest_framework.FilterSet):
    """
    过滤的字段为 name，用于为不同的apk实现不同的接口。
    
    [FieldFilter] URL 格式为： http://www.zhuiyinggu.com:33333/apk/apk_version/?name=Face2Face
    """
    
    class Meta:
        model = Video
        fields = ['name',]


# Video 版本控制
# --------------
class VideoViewSet(viewsets.ModelViewSet):
    """
    用于进行 game管理。
    对应 Game 模型，通过过滤器对不同的软件提供不同的接口。
    提供返回某一apk的版本，或者返回某一apk的最新版本。
    只有systemuser可以增加、修改、删除apk版本信息。
    其他普通用户和未登录用户只有查看权限。   
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    #lookup_field = 'name'
     
    permission_classes = (IsAuthenticatedOrReadOnly, IsSystemUserOrReadOnly, )    
    
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    
    filter_class = VideoFilter
        
    ordering_fields = ('name',) 
    ordering = ('name',)
    search_fields = ('name',)

    # # 按用户限流
    # throttle_classes = (UserRateThrottle,)
    # # 按作用域限流
    # throttle_scope = 'user'
             
       
    def update(self, request, *args, **kwargs):
        """
        覆写 update()
        设置partial属性为True使其序列化时字段可以部分更新
        """
        partial = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)






