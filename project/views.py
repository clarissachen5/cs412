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

from .forms import (
    CreateMealPlanEntryForm,
    CreateMealIdeaForm,
    CreateCreatorForm,
    CreateMealPlanForm,
    UpdateMealIdeaForm,
    CreateIngredientForm,
    CreateStoreForm,
    CreateMealIngredientForm,
)

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

    def get_image_url(self):
        """sets the image url depending on whether an image file exists or not."""
        if self.image:
            return self.image.url
        return ""


class CreatorMealIdeasView(LoginRequiredMixin, DetailView):
    """Define a view class to show the meal ideas for one Creator."""

    model = Creator
    template_name = "project/show_creator_meal_ideas.html"
    context_object_name = "creator"

    def get_login_url(self):
        """Return the URL for this app's login page."""

        return reverse("login_page")

    def get_object(self):
        """Return the Creator corresponding to the User."""
        user = self.request.user
        creator = Creator.objects.get(user=user)
        return creator

    def get_image_url(self):
        """sets the image url depending on whether an image file exists or not."""
        if self.image:
            return self.image.url
        return ""

    def get_context_data(self, **kwargs):
        """Provides the meal ideas for the Creator"""
        context = super().get_context_data(**kwargs)
        creator = self.get_object()

        mealIdeas = MealIdea.objects.filter(creator=creator)
        context["meal_ideas"] = mealIdeas
        return context


class MealPlanListView(ListView):
    """Define a view class to show all Meal Plans."""

    model = MealPlan
    template_name = "project/show_all_meal_plans.html"
    context_object_name = "meal_plans"


class CreatorMealPlansView(LoginRequiredMixin, DetailView):
    """Define a view class to show the meal plans for one Creator."""

    model = Creator
    template_name = "project/show_creator_meal_plans.html"
    context_object_name = "creator"

    def get_login_url(self):
        """Return the URL for this app's login page."""

        return reverse("login_page")

    def get_object(self):
        """Return the Creator corresponding to the User."""
        user = self.request.user
        creator = Creator.objects.get(user=user)
        return creator

    def get_context_data(self, **kwargs):
        """Provides the meal ideas for the Creator"""
        context = super().get_context_data(**kwargs)
        creator = self.get_object()

        meal_plans = MealPlan.objects.filter(creator=creator)
        context["meal_plans"] = meal_plans
        return context


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


class CreateMealPlanEntryView(LoginRequiredMixin, CreateView):
    """A view to handle the creation of a meal entry, aka adding a meal idea to a meal plan."""

    form_class = CreateMealPlanEntryForm
    template_name = "project/create_meal_plan_entry_form.html"

    def get_login_url(self):
        """Return the URL for this app's login page."""

        return reverse("login_page")

    def get_context_data(self, **kwargs):
        """Get the meal idea to add to a meal plan."""
        context = super().get_context_data(**kwargs)
        meal_idea = MealIdea.objects.get(pk=self.kwargs["pk"])
        context["meal_idea"] = meal_idea

        meal_plans = MealPlan.objects.all()
        context["meal_plans"] = meal_plans
        return context

    def get_object(self):
        """Return the meal idea for this meal plan entry."""
        meal_idea = MealIdea.objects.get(pk=self.kwargs["pk"])
        return meal_idea

    def get_image_url(self):
        """sets the image url depending on whether an image file exists or not."""
        if self.image:
            return self.image.url
        return ""

    def get_success_url(self):
        """Provide a URL to redirect to after creating a new meal plan entry."""

        return reverse("show_all_meal_ideas")

    def form_valid(self, form):
        """This method handles the form submission and saves the new object to the Django database."""

        print(form.cleaned_data)
        meal_idea = self.get_object()
        form.instance.meal_idea = meal_idea

        meal_idea = form.save()
        # saves the meal idea
        response = super().form_valid(form)

        return response


class CreateMealIdeaView(LoginRequiredMixin, CreateView):
    """A view to handle the creation of a meal idea.
    (1) display the HTML form to user (GET)
    (2) process the form submission and store the new Post object (POST)"""

    form_class = CreateMealIdeaForm
    template_name = "project/create_meal_idea_form.html"

    def get_login_url(self):
        """Return the URL for this app's login page."""

        return reverse("login_page")

    def get_object(self):
        """Return the Creator corresponding to the User."""
        user = self.request.user
        creator = Creator.objects.get(user=user)
        return creator

    def get_context_data(self, **kwargs):
        """Return context with creator set."""
        context = super().get_context_data(**kwargs)
        creator = self.get_object()
        context["creator"] = creator
        return context

    def get_success_url(self):
        """Provide a URL to redirect to after creating a new Meal Idea."""
        return reverse("show_all_meal_ideas")

    def form_valid(self, form):
        """This method handles the form submission and saves the new object to the Django database."""

        print(form.cleaned_data)
        creator = self.get_object()
        form.instance.creator = creator

        meal_idea = form.save()

        ingredients = form.instance.ingredients
        print(ingredients)

        response = super().form_valid(form)
        # ingredientsList = ingredients.split(", ")
        # print(ingredientsList)

        # for i in ingredientsList:
        # similar to mini insta adding images to a post, review that

        # saves the meal idea

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
        """Redirects to show all meal ideas once made successfully."""

        return reverse("show_all_meal_ideas")

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


class CreateMealPlanView(LoginRequiredMixin, CreateView):
    """A view to handle the creation of a meal plan.
    (1) display the HTML form to user (GET)
    (2) process the form submission and store the new Post object (POST)"""

    form_class = CreateMealPlanForm
    template_name = "project/create_meal_plan_form.html"

    def get_login_url(self):
        """Return the URL for this app's login page."""

        return reverse("login_page")

    def get_object(self):
        """Return the Creator corresponding to the User."""
        user = self.request.user
        creator = Creator.objects.get(user=user)
        return creator

    def get_success_url(self):
        """Provide a URL to redirect to after creating a new Meal Plan."""
        return reverse("show_all_meal_plans")

    def form_valid(self, form):
        """This method handles the form submission and saves the new object to the Django database."""

        print(form.cleaned_data)
        creator = self.get_object()
        form.instance.creator = creator
        form.save()

        response = super().form_valid(form)

        return response


class DeleteMealPlanView(LoginRequiredMixin, DeleteView):
    """View class to delete a meal plan and all corresponding MealPlanEntry objects."""

    model = MealPlan
    template_name = "project/delete_meal_plan_form.html"

    def get_login_url(self):
        """Return the URL for this app's login page."""

        return reverse("login_page")

    def get_success_url(self):
        """Return the URL to redirect after a successful delete."""

        return reverse("show_all_meal_plans")


class DeleteMealPlanEntryView(LoginRequiredMixin, DeleteView):
    """View class to delete a MealPlanEntry from a meal plan."""

    model = MealPlanEntry
    template_name = "project/delete_meal_plan_entry_form.html"
    context_object_name = "meal_plan_entry"

    def get_login_url(self):
        """Return the URL for this app's login page."""

        return reverse("login_page")

    def get_success_url(self):
        """Return the URL to redirect after a successful delete."""
        pk = self.kwargs["pk"]
        meal_plan_entry = MealPlanEntry.objects.get(pk=pk)
        meal_plan = meal_plan_entry.meal_plan
        return reverse("show_meal_plan", kwargs={"pk": meal_plan.pk})


class UpdateMealIdeaView(LoginRequiredMixin, UpdateView):
    """View class to handle update of a Meal Idea based on its PK"""

    model = MealIdea
    form_class = UpdateMealIdeaForm
    template_name = "project/update_meal_idea_form.html"
    context_object_name = "meal_idea"

    def get_login_url(self):
        """Return the URL for this app's login page."""

        return reverse("login_page")

    def get_success_url(self):
        """Return the URL to redirect after a successful update."""

        return reverse("show_all_meal_ideas")


class CreateIngredientView(CreateView):
    """Define a class for creating a new Ingredient."""

    template_name = "project/create_ingredient_form.html"
    form_class = CreateIngredientForm
    model = Ingredient

    def get_success_url(self):
        """Redirects to show ingredients once made successfully."""

        return reverse("show_all_ingredients")

    def form_valid(self, form):
        """This method handles the form submission and saves the new object to the Django database."""

        print(form.cleaned_data)
        form.save()

        response = super().form_valid(form)

        return response


class CreateMealIngredientView(CreateView):
    """Define a class for creating a new MealIngredient."""

    template_name = "project/create_meal_ingredient_form.html"
    form_class = CreateMealIngredientForm
    model = MealIngredient
    context_object_name = "meal_idea"

    def get_object(self):
        """Return the meal idea corresponding to the ingredient."""
        pk = self.kwargs["pk"]
        meal_idea = MealIdea.objects.get(pk=pk)

        return meal_idea

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meal_idea"] = self.get_object()
        return context

    def get_success_url(self):
        """Redirects to show meal ideas once made successfully."""

        return reverse("show_all_meal_ideas")

    def form_valid(self, form):
        """This method handles the form submission and saves the new object to the Django database."""

        print(form.cleaned_data)
        meal_idea = self.get_object()
        form.instance.meal_idea = meal_idea
        form.save()

        response = super().form_valid(form)

        return response


class DeleteIngredientView(DeleteView):
    """View class to delete a meal plan and all corresponding MealPlanEntry objects."""

    model = Ingredient
    template_name = "project/delete_ingredient_form.html"

    def get_success_url(self):
        """Return the URL to redirect after a successful delete."""

        return reverse("show_all_ingredients")


class CreateStoreView(CreateView):
    """Define a class for creating a new Store."""

    template_name = "project/create_store_form.html"
    form_class = CreateStoreForm
    model = Store

    def get_success_url(self):
        """Redirects to show ingredients once made successfully."""

        return reverse("show_all_ingredients")

    def form_valid(self, form):
        """This method handles the form submission and saves the new object to the Django database."""

        print(form.cleaned_data)
        form.save()

        response = super().form_valid(form)

        return response
