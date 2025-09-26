from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Profile


class ProfileListView(ListView):
    """Define a view class to show all Profiles."""

    model = Profile
    template_name = "mini_insta/show_all_profiles.html"
    context_object_name = "profiles"
