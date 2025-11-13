# File: dadjokes/models.py
# Author: Clarissa Chen (clchen5@bu.edu), 11/13/2025
# Description: Creates models for the dadjokes application.

from django.db import models

# Create your models here.


class Joke(models.Model):
    """Encapsulate the data of a Joke."""

    text = models.TextField(blank=True)
    name = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a string representation of this model instance."""
        return f"text: {self.text}, name: {self.name}, timestamp: {self.timestamp}"


class Picture(models.Model):
    """Encapsulate the data of a Picture."""

    image_url = models.TextField(blank=True)
    name = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a string representation of this model instance."""
        return f"image_url: {self.image_url}, name: {self.name}, timestamp: {self.timestamp}"
