# File: restaurant/urls.py
# Author: Clarissa Chen (clchen5@bu.edu), 9/18/2025
# Description: URL patterns specific to the restaurant application
from django.urls import path
from django.conf import settings
from . import views

# URL patterns specific to the restaurant app:
urlpatterns = [
    path(r"main", views.main_page, name="main_page"),  # paths to main page
    path(r"order", views.order_page, name="order_page"),  # paths to order page
    path(
        r"confirmation", views.confirmation_page, name="confirmation_page"
    ),  # paths to confirmation page
]
