# File: project/forms.py
# Author: Clarissa Chen (clchen5@bu.edu), 12/2/2025
# Description: Define the forms that we use for create/update/delete operations for project.

from django import forms
from .models import *


class CreateMealPlanEntryForm(forms.ModelForm):
    """A form to add a meal plan entry to the database."""

    class Meta:
        """Associate this form with the Post model from our database."""

        model = MealPlanEntry
        fields = ["meal_plan"]


class CreateMealIdeaForm(forms.ModelForm):
    """A form to add a meal idea to the database."""

    class Meta:
        """'Associate this form with the Meal Idea model from our database."""

        model = MealIdea
        fields = ["name", "ingredients", "link", "image"]


class CreateCreatorForm(forms.ModelForm):
    """A form to handle creating a new Creator."""

    class Meta:
        """Associate this form with the Creator model in our database."""

        model = Creator
        fields = ["last_name", "first_name", "email"]
