# File: mini_insta/views.py
# Author: Clarissa Chen (clchen5@bu.edu), 9/26/2025
# Description: Configures views specific to mini_insta app.


from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from .models import Profile, Post, Photo
from .forms import CreatePostForm
from django.urls import reverse


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


class PostDetailView(DetailView):
    """Define a view class to show one post"""

    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"


class CreatePostView(CreateView):
    """A view to handle creation of a new Post.
    (1) display the HTML form to user (GET)
    (2) process the form submission and store the new Post object (POST)"""

    form_class = CreatePostForm
    template_name = "mini_insta/create_post_form.html"

    def get_context_data(self, **kwargs):
        """Return the primary key of the Profile making the post."""
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.kwargs["pk"])
        context["profile"] = profile
        return context

    def get_success_url(self):
        """Provide a URL to redirect to after creating a new Post."""

        # call reverse to generate the URL for this Post's associated Profile.
        return reverse("show_profile", kwargs={"pk": self.kwargs["pk"]})

    def form_valid(self, form):
        """This method handles the form submission and saves the new object to the Django database.
        We need to add the foreign key (of the Profile) to the Post object before saving it to the database.
        """
        print(form.cleaned_data)

        # retrieve the PK from the URL pattern
        pk = self.kwargs["pk"]
        profile = Profile.objects.get(pk=pk)
        # attach this profile to the post
        form.instance.profile = profile  # set the PK

        # saves the post
        response = super().form_valid(form)

        image_url = self.request.POST.get("image_url")
        if image_url:
            Photo.objects.create(post=self.object, image_url=image_url)
        # delegate the work to the superclass method form_valid:
        return response
