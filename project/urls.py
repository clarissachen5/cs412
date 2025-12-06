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
]
