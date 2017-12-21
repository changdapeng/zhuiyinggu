"""
blog/serializers.py

Blog 序列化器：
实现相应object的URL返回。
"""
from django.contrib.auth import get_user_model
User = get_user_model() 

from rest_framework import serializers

from blog.models import Blog

import markdown



# Blog模型对应的序列化器
# ----------------------------
class BlogSerializer(serializers.HyperlinkedModelSerializer):
    """
    对全部字段序列化，并返回每个object对应的URL
    """   
    url = serializers.HyperlinkedIdentityField(view_name='blog-detail', lookup_field='pk')
    
    class Meta:
        model = Blog
        fields = ('title', 'subtitle', 'content', 'author', 'create_date', 'change_date', 'address', 'url')

    def create(self, validated_data):
        """
        覆写create()
        创建Blog实例的时候,使用Markdown格式化content文本
        """
        blog = Blog.objects.create(**validated_data)
        blog.content = markdown.markdown(validated_data.get('content', blog.content))
        blog.save()
        return blog

    def update(self, instance, validated_data):
        """
        覆写 update()
        创建Blog实例的时候,使用Markdown格式化content文本
        """
        blog = instance
        blog.title = validated_data.get('title', blog.title)
        blog.subtitle = validated_data.get('subtitle', blog.subtitle)
        blog.content = markdown.markdown(validated_data.get('content', blog.content))
        blog.change_date = validated_data.get('change_date', blog.change_date)
        blog.address = validated_data.get('address', blog.address)

        blog.save()
        return blog






