# File: project/views.py
# Author: Clarissa Chen (clchen5@bu.edu), 11/25/2025
# Description: Configures views specific to project app.


from django.shortcuts import render, redirect

from django.views.generic import (
    ListView,
    DetailView,
)

from .models import (
    MealIdea,
    MealIngredient,
    MealPlan,
    Ingredient,
    Creator,
    Store,
    MealPlanEntry,
)


class MealIdeaListView(ListView):
    """Define a view class to show all MealIdeas."""

    model = MealIdea
    template_name = "project/show_all_meal_ideas.html"
    context_object_name = "meal_ideas"


class MealPlanListView(ListView):
    """Define a view class to show all Meal Plans."""

    model = MealPlan
    template_name = "project/show_all_meal_plans.html"
    context_object_name = "meal_plans"
