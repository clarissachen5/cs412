# File: voter_analytics/urls.py
# Author: Clarissa Chen (clchen5@bu.edu), 10/30/2025
# Description: Specifies the url paths for voter_analytics

from django.urls import path
from . import views


# URL patterns specific to the mini_insta app:
urlpatterns = [
    path("", views.VotersListView.as_view(), name="voters"),
    path("voters", views.VotersListView.as_view(), name="voters_list"),
    path(r"voters/<int:pk>", views.VoterDetailView.as_view(), name="voter_detail"),
]
