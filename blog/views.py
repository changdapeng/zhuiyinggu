import re

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()
import django_filters

from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import detail_route, list_route
from rest_framework.throttling import UserRateThrottle, ScopedRateThrottle 

from guardian.models import UserObjectPermission
from guardian.shortcuts import assign_perm, get_perms 

from blog.models import Tag, Blog
from blog.serializers import TagSerializer, BlogSerializer






class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'name'



class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'title'
