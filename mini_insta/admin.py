# File: mini_insta/admin.py
# Author: Clarissa Chen (clchen5@bu.edu), 9/26/2025
# Description: Registers Profile with Django admin so I can use admin to create Profiles

from django.contrib import admin

# Register your models here.
from .models import Profile, Post, Photo, Follow, Comment, Like

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Photo)
admin.site.register(Follow)
admin.site.register(Comment)
admin.site.register(Like)
