from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import time
import random

# Create your views here.
quotes = [
    "Take that, you ruffian!",
    "I simply cannot let such a crime against fabulosity go uncorrected",
    "Look upon me Equestria, for I am Rarity!",
]
images = [
    "https://upload.wikimedia.org/wikipedia/en/thumb/b/ba/Rarity_in_S1E19.png/250px-Rarity_in_S1E19.png",
    "https://cdn.staticneo.com/w/mylittlepony/thumb/Rarityy.png/300px-Rarityy.png",
    "https://i.ytimg.com/vi/roXJuJfbdG4/maxresdefault.jpg",
]


def quote(request):
    """Fund to respond to the "home" request."""
    response_text = f"""
    <html>
    <h1>My Little Pony</h1>
    </html>
    """

    return HttpResponse(response_text)


def quote_page(request):
    """Respond to the URL '', delegate work to a template. Displays one quote and one image"""
    index = random.randint(0, len(quotes) - 1)

    template_name = "quotes/quote.html"
    context = {
        "quote": quotes[index],
        "image": images[index],
    }

    return render(request, template_name, context)


def show_all_page(request):
    """Respond to the URL 'show_all', delegate work to a template"""

    template_name = "quotes/quote.html"
    context = {
        "quotes": quotes,
        "images": images,
    }

    return render(request, template_name, context)


def about_page(request):
    """Respond to the URL 'about', delegate work to a template."""

    template_name = "quotes/about.html"
    # a dict of context variables (key-value pairs)
    context = {
        "name": "Rarity",
    }
    return render(request, template_name, context)
