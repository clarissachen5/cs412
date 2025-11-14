# File: dadjokes/views.py
# Author: Clarissa Chen (clchen5@bu.edu), 11/13/2025
# Description: Configures views specific to dadjokes app.


from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from .models import Joke, Picture
import random


class JokeTemplateView(TemplateView):
    """Define a view class to show one joke"""

    model = Joke
    template_name = "dadjokes/show_joke.html"
    context_object_name = "joke"

    def get_context_data(self, **kwargs):
        """Provides text and picture for a random joke."""
        context = super().get_context_data(**kwargs)

        jokes = Joke.objects.all()
        pictures = Picture.objects.all()
        jokeList = []
        picturesList = []

        for j in jokes:
            jokeList.append(j)
        for p in pictures:
            picturesList.append(p)

        context["joke"] = random.choices(jokeList)
        context["picture"] = random.choices(picturesList)
        return context


def randomJoke(request):
    """Displays a random joke and picture"""
    template_name = "dadjokes/show_random_joke.html"

    joke = Joke.objects.order_by(
        "?"
    ).first()  # randomizes order of queries and grabs first
    picture = Picture.objects.order_by("?").first()

    context = {
        "joke": joke,
        "picture": picture,
    }
    return render(request, template_name=template_name, context=context)


class JokesListView(ListView):
    """Define a view class to show all Jokes."""

    model = Joke
    template_name = "dadjokes/show_all_jokes.html"
    context_object_name = "jokes"


class JokeDetailView(DetailView):
    """Define a view class to show one Joke."""

    model = Joke
    template_name = "dadjokes/show_joke.html"
    context_object_name = "joke"

    def get_object(self):
        """Return the Joke object of the Joke."""

        if "pk" in self.kwargs:
            joke = Joke.objects.get(pk=self.kwargs["pk"])
            return joke


class PictureListView(ListView):
    """Define a view class to show all Pictures."""

    model = Picture
    template_name = "dadjokes/show_all_pictures.html"
    context_object_name = "pictures"


class PictureDetailView(DetailView):
    """Define a view class to show one Picture."""

    model = Picture
    template_name = "dadjokes/show_picture.html"
    context_object_name = "picture"

    def get_object(self):
        """Return the Picture object of the Picture."""

        if "pk" in self.kwargs:
            picture = Picture.objects.get(pk=self.kwargs["pk"])
            return picture
