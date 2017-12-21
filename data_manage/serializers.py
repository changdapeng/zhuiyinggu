"""
data_manage/serializers.py

Game、Movie、Music、Book、Video 的序列化器：
实现相应object的URL返回。
"""
from django.contrib.auth import get_user_model
User = get_user_model() 

from rest_framework import serializers

from data_manage.models import Game, Movie, Music, Book, Video



# Game 模型对应的序列化器
# -----------------------
class GameSerializer(serializers.HyperlinkedModelSerializer):
    """
    对全部字段序列化，并返回每个object对应的URL
    """   
    url = serializers.HyperlinkedIdentityField(view_name='game-detail', lookup_field='pk')
    
    class Meta:
        model = Game
        fields = ('name', 'description', 'game_type', 'game_step', 'seed_address', 
            'seed_type', 'creator', 'create_date', 'update_date', 'url')



# Movie 模型对应的序列化器
# -----------------------
class MovieSerializer(serializers.HyperlinkedModelSerializer):
    """
    对全部字段序列化，并返回每个object对应的URL
    """   
    url = serializers.HyperlinkedIdentityField(view_name='movie-detail', lookup_field='pk')
    
    class Meta:
        model = Movie
        fields = ('name', 'description', 'movie_type', 'movie_step', 'seed_address', 
            'seed_type', 'creator', 'create_date', 'update_date', 'url')



# Music 模型对应的序列化器
# -----------------------
class MusicSerializer(serializers.HyperlinkedModelSerializer):
    """
    对全部字段序列化，并返回每个object对应的URL
    """   
    url = serializers.HyperlinkedIdentityField(view_name='music-detail', lookup_field='pk')
    
    class Meta:
        model = Music
        fields = ('name', 'description', 'singer', 'album', 'music_format', 'music_type', 
            'music_step', 'music_file', 'creator', 'creator', 'create_date', 'update_date', 'url')



# Book 模型对应的序列化器
# -----------------------
class BookSerializer(serializers.HyperlinkedModelSerializer):
    """
    对全部字段序列化，并返回每个object对应的URL
    """   
    url = serializers.HyperlinkedIdentityField(view_name='book-detail', lookup_field='pk')
    
    class Meta:
        model = Book
        fields = ('name', 'description', 'author', 'book_type', 'book_step', 
            'book_file', 'creator', 'create_date', 'update_date', 'url')



# Video 模型对应的序列化器
# -----------------------
class VideoSerializer(serializers.HyperlinkedModelSerializer):
    """
    对全部字段序列化，并返回每个object对应的URL
    """   
    url = serializers.HyperlinkedIdentityField(view_name='video-detail', lookup_field='pk')
    
    class Meta:
        model = Video
        fields = ('name', 'description', 'video_type', 'video_step', 'seed_address', 
            'seed_type', 'creator', 'create_date', 'update_date', 'url')