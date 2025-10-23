# File: mini_insta/urls.py
# Author: Clarissa Chen (clchen5@bu.edu), 9/26/2025
# Description: Specifies the url paths for mini_insta

from django.urls import path
from .views import *  # ProfileListView, ProfileDetailView, PostDetailView

from django.contrib.auth import views as auth_views

# URL patterns specific to the mini_insta app:
urlpatterns = [
    path("", ProfileListView.as_view(), name="show_all_profiles"),
    path("profile/<int:pk>", ProfileDetailView.as_view(), name="show_profile"),
    path("profile", ProfileDetailView.as_view(), name="show_logged_in_profile"),
    path("post/<int:pk>", PostDetailView.as_view(), name="show_post"),
    path("profile/create_post", CreatePostView.as_view(), name="create_post"),
    path("profile/update", UpdateProfileView.as_view(), name="update_profile"),
    path("post/<int:pk>/delete", DeletePostView.as_view(), name="delete_post"),
    path("post/<int:pk>/update", UpdatePostView.as_view(), name="update_post"),
    path("photo/<int:pk>/delete", DeletePhotoView.as_view(), name="delete_photo"),
    path("photo/<int:pk>/create_photo", CreatePhotoView.as_view(), name="create_photo"),
    path(
        "profile/<int:pk>/followers",
        ShowFollowersDetailView.as_view(),
        name="followers",
    ),
    path(
        "profile/<int:pk>/following",
        ShowFollowingDetailView.as_view(),
        name="following",
    ),
    path("profile/feed", PostFeedListView.as_view(), name="feed"),
    path("profile/search", SearchView.as_view(), name="search"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="mini_insta/login.html"),
        name="login_page",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="show_all_profiles"),
        name="logout_page",
    ),
]
