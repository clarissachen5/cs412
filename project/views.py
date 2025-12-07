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

from .forms import CreateMealPlanEntryForm, CreateMealIdeaForm, CreateCreatorForm

from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login


class MealIdeaListView(ListView):
    """Define a view class to show all MealIdeas."""

    model = MealIdea
    template_name = "project/show_all_meal_ideas.html"
    context_object_name = "meal_ideas"


class CreatorDetailView(DetailView):
    """Define a view class to show the meal ideas for one Creator."""

    model = Creator
    template_name = "project/show_creator_meal_ideas.html"
    context_object_name = "creator"

    def get_context_data(self, **kwargs):
        """Provides the meal ideas for the Creator"""
        context = super().get_context_data(**kwargs)

        mealIdeas = MealIdea.objects.filter(Creator=self.kwargs["pk"])
        context["mealIdeas"] = mealIdeas
        return context


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


class IngredientListView(ListView):
    """'Define a view class to show all ingredients"""

    model = Ingredient
    template_name = "project/show_all_ingredients.html"
    context_object_name = "ingredients"


class GroceryList(DetailView):
    """Define a view class to show the ingredients lists for a meal plan"""

    model = MealPlan
    template_name = "project/grocery_list.html"
    context_object_name = "meal_plan"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        mealPlan = MealPlan.objects.get(pk=self.kwargs["pk"])
        mealPlanEntries = MealPlanEntry.objects.filter(meal_plan=mealPlan)

        context["meal_entries"] = mealPlanEntries
        storeLists = {}
        for entry in mealPlanEntries:
            meal_ingredients = MealIngredient.objects.filter(
                meal_idea=entry.meal_idea
            )  # gets the meal ingredients for the MealPlanEntry's meal_idea
            for i in meal_ingredients:
                ingredient = Ingredient.objects.get(pk=i.ingredient.pk)
                store = Store.objects.get(pk=ingredient.store.pk)

                if store.name in storeLists:
                    if ingredient.name in storeLists[store.name]:
                        storeLists[store.name][ingredient.name][1] += i.quantity
                    else:
                        storeLists[store.name][ingredient.name] = [
                            ingredient.unit,
                            i.quantity,
                        ]
                else:
                    storeLists[store.name] = {}
                    storeLists[store.name][ingredient.name] = [
                        ingredient.unit,
                        i.quantity,
                    ]

        context["storeLists"] = storeLists
        return context

        # if ingredient.name in mealPlanIngredients:
        #     mealPlanIngredients[ingredient.name][2] += i.quantity
        # else:
        #     mealPlanIngredients[ingredient.name] = [ingredient.unit, ingredient.store, i.quantity]


# """add context for grocery ingredients lists by store from the meal plan """


class CreateMealPlanEntryView(CreateView):
    """A view to handle the creation of a meal entry, aka adding a meal idea to a meal plan."""

    form_class = CreateMealPlanEntryForm
    template_name = "project/create_meal_plan_entry_form.html"

    def get_success_url(self):
        """Provide a URL to redirect to after creating a new meal plan entry."""

        return reverse("show_all_meal_ideas")


class CreateMealIdeaView(CreateView):
    """A view to handle the creation of a meal idea.
    (1) display the HTML form to user (GET)
    (2) process the form submission and store the new Post object (POST)"""

    form_class = CreateMealIdeaForm
    template_name = "project/create_meal_idea_form.html"

    def get_success_url(self):
        """Provide a URL to redirect to after creating a new Meal Idea."""
        return reverse("show_all_meal_ideas")

    def form_valid(self, form):
        """This method handles the form submission and saves the new object to the Django database."""

        print(form.cleaned_data)
        creator = Creator.objects.get(pk=1)  # placeholder for now
        form.instance.creator = creator

        meal_idea = form.save()
        # saves the meal idea
        response = super().form_valid(form)

        return response


class LogoutConfirmationView(TemplateView):
    """Define a class for the Logout Confirmation."""

    template_name = "project/logged_out.html"


class CreateCreatorView(CreateView):
    """Define a class for creating a new Creator."""

    template_name = "project/create_creator_form.html"
    form_class = CreateCreatorForm
    model = Creator

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_form"] = UserCreationForm()
        return context

    def get_absolute_url(self):
        """Redirects to show meal ideas once made successfully."""

        return reverse("creator_meal_ideas", kwargs={"pk", self.pk})

    def form_valid(self, form):
        """This method handles the form submission and saves the new Creator object to the Django database."""

        user_form = UserCreationForm(self.request.POST)

        if not user_form.is_valid():
            context = self.get_context_data(form=form)
            context["user_form"] = user_form
            return self.render_to_response(context)
        user = user_form.save()

        login(self.request, user, backend="django.contrib.auth.backends.ModelBackend")

        form.instance.user = user

        response = super().form_valid(form)
        return response
