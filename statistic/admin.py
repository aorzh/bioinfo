from django.contrib import admin
from statistic.models import UserProfile, Post


class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]

admin.site.register(Post, PostAdmin)

admin.site.register(UserProfile)
