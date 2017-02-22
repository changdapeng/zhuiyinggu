"""
blog/models.py

自定义Blog模型
"""
from django.db import models
from django.conf import settings



# blog 模型
# ---------
class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blog_author')
    content = models.TextField()



    def __str__(self):
        return self.title
