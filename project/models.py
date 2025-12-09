# File: project/models.py
# Author: Clarissa Chen (clchen5@bu.edu), 11/24/2025
# Description: Defines the models for project app.


from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Creator(models.Model):
    """Encapsulate the data of a Creator"""

    last_name = models.TextField(blank=True)
    first_name = models.TextField(blank=True)
    email = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of this model instance."""
        return f"last_name: {self.last_name}, first_name: {self.first_name}, email: {self.email}"

    def get_absolute_url(self):
        """Display all meal ideas for creator"""
        return reverse("show_creator_meal_ideas", kwargs={"pk": self.pk})


class Store(models.Model):
    """Encapsulate the data of a Store"""

    name = models.TextField(blank=True)

    def __str__(self):
        """Return a string representation of this model instance."""
        return f"name: {self.name}"


class MealIdea(models.Model):
    """Encapsulate the data of a MealIdea by a user"""

    name = models.TextField(blank=True)
    ingredients = models.TextField(blank=True)
    link = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)

    # could at timestamp
    def __str__(self):
        """Return a string representation of this model instance."""
        return f"name: {self.name}, ingredients: {self.ingredients}, link: {self.link}, creator: {self.creator}"

    def get_image_url(self):
        """returns url for the image file"""
        return self.image.url


class Ingredient(models.Model):
    """Encapsulate the data of an Ingredient by a user"""

    name = models.TextField(blank=True)
    unit = models.TextField(blank=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of this model instance."""
        return f"name: {self.name}, unit: {self.unit}, store: {self.store}"


class MealIngredient(models.Model):
    """Encapsulate the data of a MealIngredient by a user"""

    meal_idea = models.ForeignKey(MealIdea, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True)

    def __str__(self):
        """Return a string representation of this model instance."""
        return f"meal_indea: {self.meal_idea}, ingredient: {self.ingredient}, quantity: {self.quantity}"


class MealPlan(models.Model):
    """Encapsulate the data of a MealPlan by a user"""

    name = models.TextField(blank=True)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representaion of this model instance."""
        return f"meal plan name: {self.name}"


class MealPlanEntry(models.Model):
    """Encapsulate the data of a MealPlanEntry for a MealPlan."""

    meal_plan = models.ForeignKey(
        MealPlan, on_delete=models.CASCADE, related_name="entries"
    )  # related name deletes all meal plan entries associated with a meal plan when a meal plan is deleted
    meal_idea = models.ForeignKey(MealIdea, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representaion of this model instance."""
        return f"meal plan name: {self.meal_plan} meal_idea: {self.meal_idea}"
