"""
data_manage/admin.py
"""

from django.contrib import admin

from data_manage.models import Data



# Data Admin管理界面管理器
# ------------------------------

class DataAdmin(admin.ModelAdmin):

    list_display = ('name', 'description', 'step', 'data_type', 'size', 'creator', 'create_date', 'address_type', 'address', 'path',)
    list_filter = ('data_type', 'step', 'creator', 'create_date',)
    fieldsets = (
        ('Data info', {'fields': ('name', 'description', 'step', 'data_type', 'size', 'address_type', 'address', 'path',)}),
        ('create info', {'fields': ('creator', 'create_date',)}),
    )
    search_fields = ('name', 'path', 'step', 'data_type')
    ordering = ('name', 'size',)



admin.site.register(Data, DataAdmin)
