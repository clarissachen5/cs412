# File: restaurant/urls.py
# Author: Clarissa Chen (clchen5@bu.edu), 9/18/2025
# Description: URL patterns specific to the restaurant application
from django.urls import path
from django.conf import settings
from . import views

# URL patterns specific to the restaurant app:
urlpatterns = [
    path(r"main", views.main, name="main"),  # url path to main page
    path(r"order", views.order, name="order"),  # url path to order page
    path(
        r"confirmation", views.confirmation, name="confirmation"
    ),  # url path to confirmation page
]
