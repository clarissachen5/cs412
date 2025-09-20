# File: quotes/views.py
# Author: Clarissa Chen (clchen5@bu.edu), 9/16/2025
# Description: Configures views specific to quotes app

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import random

quotes = [
    "Take that, you ruffian!",
    "I simply cannot let such a crime against fabulosity go uncorrected",
    "Look upon me Equestria, for I am Rarity!",
    "Thank you Twilight. But don't get any ideas about my gem! I know where you live.",
    "It's mine!",
]
images = [
    "https://upload.wikimedia.org/wikipedia/en/thumb/b/ba/Rarity_in_S1E19.png/250px-Rarity_in_S1E19.png",
    "https://cdn.staticneo.com/w/mylittlepony/thumb/Rarityy.png/300px-Rarityy.png",
    "https://i.ytimg.com/vi/roXJuJfbdG4/maxresdefault.jpg",
    "https://i.ytimg.com/vi/Ue0oZIl2vlA/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBNJzIJQYtekUX12OPZxTe3cU5lsw",
    "https://i.ytimg.com/vi/tJiaBI3Ggkw/maxresdefault.jpg",
]


def quote(request):
    """Respond to the URL '' and 'quote', delegate work to quote template.
    Displays one quote and one image"""

    index = random.randint(0, len(quotes) - 1)
    # picks a random index for the quote and correspnding image

    template_name = "quotes/quote.html"
    context = {
        "quote": quotes[index],
        "image": images[index],
    }

    return render(request, template_name, context)


def show_all(request):
    """Respond to the URL 'show_all', delegate work to the show_all template"""

    template_name = "quotes/show_all.html"
    context = {
        "quotes": quotes,  # passes in all quotes and images
        "images": images,
    }

    return render(request, template_name, context)


def about(request):
    """Respond to the URL 'about', delegate work to the about template."""

    template_name = "quotes/about.html"

    context = {
        "name": "Rarity",
    }
    return render(request, template_name, context)
