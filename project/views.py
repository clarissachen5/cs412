# File: project/views.py
# Author: Clarissa Chen (clchen5@bu.edu), 11/25/2025
# Description: Configures views specific to project app.


from django.shortcuts import render, redirect

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
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

from .forms import CreateMealPlanEntryForm

from django.urls import reverse


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


class MealPlanDetailView(DetailView):
    """'Define a view class to show all meal plan entries for a selected meal plan."""

    model = MealPlan
    template_name = "project/show_meal_plan.html"
    context_object_name = "meal_plan"

    def get_context_data(self, **kwargs):
        """Provides info on what meal plan entries are associated with this meal plan"""

        context = super().get_context_data(**kwargs)

        mealPlan = MealPlan.objects.get(pk=self.kwargs["pk"])
        mealPlanEntries = MealPlanEntry.objects.filter(meal_plan=mealPlan)

        context["meal_entries"] = mealPlanEntries

        return context


class CreateMealPlanEntryView(CreateView):
    """A view to handle the creation of a meal entry, aka adding a meal idea to a meal plan."""

    form_class = CreateMealPlanEntryForm
    template_name = "project/create_meal_plan_entry_form.html"

    def get_success_url(self):
        """Provide a URL to redirect to after creating a new meal plan entry."""

        return reverse("show_all_meal_ideas")
