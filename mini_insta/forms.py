# File: mini_insta/forms.py
# Author: Clarissa Chen (clchen5@bu.edu), 10/3/2025
# Description: Define the forms that we use for create/update/delete operations for mini_insta.

from django import forms
from .models import *


class CreatePostForm(forms.ModelForm):
    """A form to add a Post to the database."""

    class Meta:
        """Associate this form with a the Post model from our database."""

        model = Post
        fields = ["caption"]


class UpdateProfileForm(forms.ModelForm):
    """A form to handle an update to a Profile."""

    class Meta:
        """Associate this form with the Profile model in our database."""

        model = Profile
        fields = ["display_name", "profile_image_url", "bio_text"]


class UpdatePostForm(forms.ModelForm):
    """A form to handle an update to a Post."""

    class Meta:
        """Associate this form with the Post model in our database."""

        model = Post
        fields = ["caption"]
