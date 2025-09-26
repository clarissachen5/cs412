# File: mini_insta/urls.py
# Author: Clarissa Chen (clchen5@bu.edu), 9/26/2025
# Description: Specifies the url paths for mini_insta

from django.urls import path
from .views import ProfileListView, ProfileDetailView

# URL patterns specific to the mini_insta app:
urlpatterns = [
    path("", ProfileListView.as_view(), name="show_all_profiles"),
    path("profile/<int:pk>", ProfileDetailView.as_view(), name="show_profile"),
]
