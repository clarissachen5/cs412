# File: dadjokes/urls.py
# Author: Clarissa Chen (clchen5@bu.edu), 11/13/2025
# Description: URL patterns specific to the dadjokes application.

from django.urls import path
from django.conf import settings
from .views import *
from . import views

urlpatterns = [
    path("", views.randomJoke, name="show_joke"),
    path("random", views.randomJoke, name="random"),
    path("jokes", JokesListView.as_view(), name="show_all_jokes"),
    path("joke/<int:pk>", JokeDetailView.as_view(), name="show_joke"),
    path("pictures", PictureListView.as_view(), name="show_all_pictures"),
    path("picture/<int:pk>", PictureDetailView.as_view(), name="show_picture"),
]
