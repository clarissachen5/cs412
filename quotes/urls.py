# File: quotes/urls.py
# Author: Clarissa Chen (clchen5@bu.edu), 9/16/2025
# Description: Configures URL patterns specific to the quotes application
from django.urls import path
from django.conf import settings
from . import views

# URL patterns specific to the quotes app:
urlpatterns = [
    path(r"", views.quote, name="quote"),  # main page
    path(r"quote", views.quote, name="quote"),  # main page
    path(r"show_all", views.show_all, name="show_all"),
    path(r"about", views.about, name="about"),
]
