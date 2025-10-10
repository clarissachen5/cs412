# File: mini_insta/urls.py
# Author: Clarissa Chen (clchen5@bu.edu), 9/26/2025
# Description: Specifies the url paths for mini_insta

from django.urls import path
from .views import *  # ProfileListView, ProfileDetailView, PostDetailView

# URL patterns specific to the mini_insta app:
urlpatterns = [
    path("", ProfileListView.as_view(), name="show_all_profiles"),
    path("profile/<int:pk>", ProfileDetailView.as_view(), name="show_profile"),
    path("post/<int:pk>", PostDetailView.as_view(), name="show_post"),
    path("profile/<int:pk>/create_post", CreatePostView.as_view(), name="create_post"),
    path("profile/<int:pk>/update", UpdateProfileView.as_view(), name="update_profile"),
    path("post/<int:pk>/delete", DeletePostView.as_view(), name="delete_post"),
    path("post/<int:pk>/update", UpdatePostView.as_view(), name="update_post"),
]
