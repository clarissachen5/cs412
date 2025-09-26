# File: mini_insta/models.py
# Author: Clarissa Chen (clchen5@bu.edu), 9/26/2025
# Description: Defines the Profile model.

from django.db import models


# Create your models here.
class Profile(models.Model):
    """Encapsulate the data of a Profile by a user"""

    username = models.TextField(blank=True)
    display_name = models.TextField(blank=True)
    profile_image_url = models.TextField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.TextField(blank=True)

    def __str__(self):
        """return a string representation of this model instance."""
        return f"username: {self.username}, display name: {self.display_name}"
