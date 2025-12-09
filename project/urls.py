# File: project/urls.py
# Author: Clarissa Chen (clchen5@bu.edu), 11/25/2025
# Description: Specifies the url paths for project app

from django.urls import path
from .views import *

from django.contrib.auth import views as auth_views

# URL patterns specific to the project app:
urlpatterns = [
    path("", MealIdeaListView.as_view(), name="show_all_meal_ideas"),
    path("mealplans", MealPlanListView.as_view(), name="show_all_meal_plans"),
    path("mealplan/<int:pk>", MealPlanDetailView.as_view(), name="show_meal_plan"),
    path("ingredients", IngredientListView.as_view(), name="show_all_ingredients"),
    path("grocerylists/<int:pk>", GroceryList.as_view(), name="show_grocery_lists"),
    path("create_meal_idea", CreateMealIdeaView.as_view(), name="create_meal_idea"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="project/login.html"),
        name="login_page",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="logout_confirmation"),
        name="logout_page",
    ),
    path(
        "logout/confirmation/",
        LogoutConfirmationView.as_view(),
        name="logout_confirmation",
    ),
    path("create_creator", CreateCreatorView.as_view(), name="create_creator"),
    path(
        "creator_meal_ideas",
        CreatorDetailView.as_view(),
        name="show_creator_meal_ideas",
    ),
    path(
        "add_to_meal_plan/<int:pk>",
        CreateMealPlanEntryView.as_view(),
        name="add_to_meal_plan",
    ),
    path("create_meal_plan", CreateMealPlanView.as_view(), name="create_meal_plan"),
    path("create_ingredient", CreateIngredientView.as_view(), name="create_ingredient"),
    path("create_store", CreateStoreView.as_view(), name="create_store"),
    path(
        "ingredient/<int:pk>/delete",
        DeleteIngredientView.as_view(),
        name="delete_ingredient",
    ),
    path(
        "mealplan/<int:pk>/delete",
        DeleteMealPlanView.as_view(),
        name="delete_meal_plan",
    ),
    path(
        "meal_plan_entry/<int:pk>/delete",
        DeleteMealPlanEntryView.as_view(),
        name="delete_meal_plan_entry",
    ),
    path(
        "meal_idea/<int:pk>/update",
        UpdateMealIdeaView.as_view(),
        name="update_meal_idea",
    ),
    path(
        "create_meal_ingredient/<int:pk>",
        CreateMealIngredientView.as_view(),
        name="create_meal_ingredient",
    ),
]
