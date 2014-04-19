from django.contrib import admin
from statistic.models import UserProfile, Post, PostAdmin, UserProfileAdmin

admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
