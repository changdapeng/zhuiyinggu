"""
blog/models.py

自定义Blog模型
"""
from django.db import models



# blog 模型
# ---------
class Blog(models.Model):
	name = models.CharField(max_length=200)
	author = models.CharField(max_length=200)


