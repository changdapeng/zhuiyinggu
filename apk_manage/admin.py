"""
apk_manage/admin.py
"""

from django.contrib import admin

from guardian.admin import GuardedModelAdmin

from apk_manage.models import ApkVersion



# ApkVersion Admin管理界面管理器
# ------------------------------
# class ApkVersionAdmin(admin.ModelAdmin):
class ApkVersionAdmin(GuardedModelAdmin):  # 使用guardian插件中的权限管理

    list_display = ('name', 'version', 'creator', 'create_data', 'address',)
    list_filter = ('name', 'creator',)
    fieldsets = (
        ('Apk info', {'fields': ('name', 'version', 'address',)}),
        ('create info', {'fields': ('creator', 'create_data',)}),
    )
    search_fields = ('name',)
    ordering = ('name','version',)



admin.site.register(ApkVersion, ApkVersionAdmin)
