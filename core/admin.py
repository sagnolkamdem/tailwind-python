from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import User, Category, Announce, Logement, Location, Comment, Visit


# Register your models here.

class SuperUser(UserAdmin):
    ordering = ['id']


admin.site.register(User, SuperUser)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'description')
    ordering = ('libelle',)
    search_fields = ('libelle',)


admin.site.register(Category, CategoryAdmin)


class AnnounceAdmin(admin.ModelAdmin):
    list_display = ('title', 'quartier', 'ville', 'region', 'created_at')
    list_filter = ('available', 'validated',)
    date_hierarchy = 'created_at'
    ordering = ('title', 'created_at')
    search_fields = ('title',)


admin.site.register(Announce, AnnounceAdmin)


class LogementAdmin(admin.ModelAdmin):
    list_display = ('superficie', 'price', 'meuble', 'announce', 'created_at')
    list_filter = ('meuble',)
    date_hierarchy = 'created_at'
    ordering = ('created_at',)
    search_fields = ('price',)


admin.site.register(Logement, LogementAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('client', 'announce', 'created_at')
    date_hierarchy = 'created_at'
    ordering = ('announce',)
    search_fields = ('client',)


admin.site.register(Location, LocationAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'author_id', 'content', 'created_at', 'announce')
    list_filter = ('author_id',)
    date_hierarchy = 'created_at'
    ordering = ('created_at',)
    search_fields = ('author_id',)


admin.site.register(Comment, CommentAdmin)
admin.site.register(Visit)