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
    template_name = "dadjokes/show_joke.html"

    joke = Joke.objects.order_by(
        "?"
    ).first()  # randomizes order of queries and grabs first
    picture = Picture.objects.order_by("?").first()

    context = {
        "joke": joke,
        "picture": picture,
    }
    return render(request, template_name=template_name, context=context)
