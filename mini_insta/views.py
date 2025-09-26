# File: mini_insta/views.py
# Author: Clarissa Chen (clchen5@bu.edu), 9/26/2025
# Description: Configures views specific to mini_insta app.


from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Profile


class ProfileListView(ListView):
    """Define a view class to show all Profiles."""

    model = Profile
    template_name = "mini_insta/show_all_profiles.html"
    context_object_name = "profiles"


class ProfileDetailView(DetailView):
    """Define a view class to show one profile"""

    model = Profile
    template_name = "mini_insta/show_profile.html"
    context_object_name = "profile"
