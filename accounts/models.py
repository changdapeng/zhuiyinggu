"""
accounts/models.py

MyUser：自定义 User
SystemUserProfile：后台用户，外键于MyUser
UserProfile：前台用户，外键于MyUser
"""

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.conf import settings



SYSTEM_USER = 'system_user' # 后台用户
COMMON_USER = 'common_user' # 普通用户



# MyUser 模型管理器
#----------------
class MyUserManager(BaseUserManager):
    def create_user(self, email, name, phone, unid, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password ...
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone,
            unid=unid,
        )
        user.is_superuser = False  # 指定此用户具有所有权限，而不显式分配它们。
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone, unid, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            name=name,
            phone=phone,
            unid=unid,
        )
        user.is_admin = True
        user.is_superuser = True  # 指定此用户具有所有权限，而不显式分配它们。
        user.save(using=self._db)
        return user



# 自定义用户类
#-------------
class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    unid = models.IntegerField(default=0)
    is_staff = models.BooleanField(default=True)  # 如果允许用户访问管理网站，则设置True。
    is_active = models.BooleanField(default=True)  # 如果用户帐户当前处于活动状态，则设置True。
    is_admin = models.BooleanField(default=False)
    type = models.CharField(max_length=20, default=COMMON_USER)
    
    objects = MyUserManager()

    USERNAME_FIELD = 'email'  # 一个字符串，表示User模型上用于唯一标识符的字段的名称
    EMAIL_FIELD = 'email'  # 一个字符串，描述User模型上电子邮件字段的名称。该值由get_email_field_name()返回，默认值为'email'。
    REQUIRED_FIELDS = ['name', 'phone', 'unid']  # 当通过createsuperuser管理命令创建一个用户时，用于提示的一个字段名称列表。

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.email
        
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


        
# 后台管理员用户
#---------------
class SystemUserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='systemuser')
    nickname = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField(null=True)
    
    def __str__(self):
        return self.user.email



# 前台普通用户
#-------------
class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user')
    nickname = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField(null=True)
    
    
    def __str__(self):
        return self.user.email
        
