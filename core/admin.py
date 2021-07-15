from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import User, Category, Announce, Logement, Location, Comment, Visit


# Register your models here.

class SuperUser(UserAdmin):
    ordering = ['id']


admin.site.register(User, SuperUser)

admin.site.register(Category)
admin.site.register(Announce)
admin.site.register(Logement)
admin.site.register(Location)
admin.site.register(Comment)
admin.site.register(Visit)
