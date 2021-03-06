"""
data_manage/admin.py
"""

from django.contrib import admin

from data_manage.models import Book, Music, Video, Movie, Game




# Game Admin管理界面管理器
# ------------------------
class GameAdmin(admin.ModelAdmin):

    list_display = ('name', 'description', 'game_type', 'game_step', 'seed_address', 'seed_type', 'creator', 'create_date', 'update_date',)
    list_filter = ('game_type', 'game_step', 'seed_type', 'create_date',)
    search_fields = ('name', 'game_type', 'game_step',)
    ordering = ('name', 'game_type',)
#    prepopulated_fields = {'slug': ('title',)}
#    raw_id_fields = ('author',)
    date_hierarchy = 'create_date'

    fieldsets = (
        ('Book info', {'fields': ('name', 'description', 'game_type', 'game_step', 'seed_address', 'seed_type',)}),
        ('create info', {'fields': ('creator', )}),
    )


admin.site.register(Game, GameAdmin)



# Movie Admin管理界面管理器
# -------------------------
class MovieAdmin(admin.ModelAdmin):

    list_display = ('name', 'description', 'movie_type', 'movie_step', 'seed_address', 'seed_type', 'creator', 'create_date', 'update_date',)
    list_filter = ('movie_type', 'movie_step', 'seed_type', 'create_date',)
    search_fields = ('name', 'movie_type', 'movie_step',)
    ordering = ('name', 'movie_type',)
    date_hierarchy = 'create_date'

    fieldsets = (
        ('Book info', {'fields': ('name', 'description', 'movie_type', 'movie_step', 'seed_address', 'seed_type',)}),
        ('create info', {'fields': ('creator', )}),
    )


admin.site.register(Movie, MovieAdmin)



# Music Admin管理界面管理器
# -------------------------
class MusicAdmin(admin.ModelAdmin):

    list_display = ('name', 'description', 'singer', 'album', 'music_format', 'music_type', 'music_step', 'music_file', 'creator', 'create_date', 'update_date',)
    list_filter = ('singer', 'album', 'music_format', 'music_type', 'music_step', 'create_date',)
    search_fields = ('name', 'singer', 'album', 'music_type', 'music_step')
    ordering = ('name', 'singer',)
    date_hierarchy = 'create_date'

    fieldsets = (
        ('Music info', {'fields': ('name', 'description', 'singer', 'album', 'music_format', 'music_type', 'music_step', 'music_file',)}),
        ('create info', {'fields': ('creator', )}),
    )


admin.site.register(Music, MusicAdmin)



# Book Admin管理界面管理器
# ------------------------
class BookAdmin(admin.ModelAdmin):

    list_display = ('name', 'description', 'author', 'book_type', 'book_step', 'book_file', 'creator', 'create_date', 'update_date',)
    list_filter = ('author', 'book_type', 'book_step', 'create_date',)
    search_fields = ('name', 'author', 'book_step', 'book_type')
    ordering = ('name', 'author',)
    date_hierarchy = 'create_date'

    fieldsets = (
        ('Book info', {'fields': ('name', 'description', 'author', 'book_type', 'book_step', 'book_file',)}),
        ('create info', {'fields': ('creator', )}),
    )


admin.site.register(Book, BookAdmin)



# Video Admin管理界面管理器
# -------------------------
class VideoAdmin(admin.ModelAdmin):

    list_display = ('name', 'description', 'video_type', 'video_step', 'seed_address', 'seed_type', 'creator', 'create_date', 'update_date',)
    list_filter = ('video_type', 'video_step', 'seed_type', 'create_date',)
    search_fields = ('name', 'video_type', 'video_step',)
    ordering = ('name', 'video_type',)
    date_hierarchy = 'create_date'

    fieldsets = (
        ('Book info', {'fields': ('name', 'description', 'video_type', 'video_step', 'seed_address', 'seed_type',)}),
        ('create info', {'fields': ('creator', )}),
    )


admin.site.register(Video, VideoAdmin)