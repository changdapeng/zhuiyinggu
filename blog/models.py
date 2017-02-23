"""
blog/models.py

自定义Blog模型
"""
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify


# Tag 模型(标签)
# --------------
class Tag(models.Model):
    name = models.CharField(max_length=10, unique=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    slug = models.SlugField(max_length=10, unique=True)

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
 








# blog 模型(博客文章)
# -------------------
class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blog_author')
    content = models.TextField()
    tag = models.ForeignKey(Tag, related_name='blog_tag')



    def __str__(self):
        return self.title
