import traceback 

from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model
User = get_user_model() 

from rest_framework import serializers

from blog.models import Tag, Blog




class TagSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='tag-detail', lookup_field='name')

    class Meta:
        model = Tag
        fields = ('name', 'likes', 'views', 'slug')




class BlogSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='blog-detail', lookup_field='title')

    class Meta:
        model = Blog
        fields = ('title', 'author', 'content', 'tag')