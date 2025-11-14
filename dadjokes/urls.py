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
    path(r"api/", RandomJokeAPIView.as_view(), name="random_joke_api"),
    path(r"api/random", RandomJokeAPIView.as_view(), name="random_joke_api"),
    path(r"api/jokes", JokeListAPIView.as_view(), name="joke_list_api"),
    path(r"api/joke/<int:pk>", JokeDetailAPIView.as_view(), name="joke_detail_api"),
    path(r"api/pictures", PictureListAPIView.as_view(), name="picture_list_api"),
    path(
        r"api/picture/<int:pk>",
        PictureDetailAPIView.as_view(),
        name="picture_detail_api",
    ),
    path(
        r"api/random_picture", RandomPictureAPIView.as_view(), name="random_picture_api"
    ),
]
