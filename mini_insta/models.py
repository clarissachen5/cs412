# File: mini_insta/models.py
# Author: Clarissa Chen (clchen5@bu.edu), 9/26/2025
# Description: Defines the Profile model.

from django.db import models
from django.urls import reverse


# Create your models here.
class Profile(models.Model):
    """Encapsulate the data of a Profile by a user"""

    username = models.TextField(blank=True)
    display_name = models.TextField(blank=True)
    profile_image_url = models.TextField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.TextField(blank=True)

    def __str__(self):
        """Return a string representation of this model instance."""
        return f"username: {self.username}, display name: {self.display_name}"

    def get_all_posts(self):
        """Return a QuerySet of Posts by this Profile."""

        posts = Post.objects.filter(profile=self).order_by(
            "-timestamp"
        )  # the negative before timestamp shows descending
        return posts

    def get_absolute_url(self):
        """Return a URL to display the updated Profile."""
        return reverse("show_profile", kwargs={"pk": self.pk})


class Post(models.Model):
    """Encapsulate the data of a Post by a user (Profile)"""

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    caption = models.TextField(blank=True)

    def __str__(self):
        """Return a string representation of this model instance."""
        return f"profile: {self.profile}, timestamp: {self.timestamp}, caption: {self.caption}"

    def get_all_photos(self):
        """Return a QuerySet of Photos for a given Post."""

        photos = Photo.objects.filter(post=self)
        return photos

    def get_absolute_url(self):
        """Return a URL to display the updated Post."""
        return reverse("show_post", kwargs={"pk": self.pk})


class Photo(models.Model):
    """Encapsulate the data of a Photo for a Post"""

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    image_file = models.ImageField(blank=True)  # an actual image

    def __str__(self):
        """Return a string representation of this model instance."""
        return f"post: {self.post}, image_url: {self.get_image_url()}, timestamp: {self.timestamp}"

    def get_image_url(self):
        """Returns the corresponding url for the image url/file."""
        if self.image_url:
            print(self.image_url)
            return self.image_url
        else:
            print(self.image_file)
            return self.image_file.url
