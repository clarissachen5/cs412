# File: project/forms.py
# Author: Clarissa Chen (clchen5@bu.edu), 12/2/2025
# Description: Define the forms that we use for create/update/delete operations for project.

from django import forms
from .models import *


class CreateMealPlanEntryForm(forms.ModelForm):
    """A form to add a meal plan entry to the database."""

    class Meta:
        """Associate this form with a the Post model from our database."""

        model = MealPlanEntry
        fields = ["meal_plan"]

