# File: project/admin.py
# Author: Clarissa Chen (clchen5@bu.edu), 11/24/2025
# Description: Registers models with Django admin so I can use admin to create objects

from django.contrib import admin

# Register your models here.
from .models import (
    MealIdea,
    Ingredient,
    MealIngredient,
    MealPlan,
    Creator,
    Store,
    MealPlanEntry,
)

admin.site.register(MealIdea)
admin.site.register(Ingredient)
admin.site.register(MealIngredient)
admin.site.register(MealPlan)
admin.site.register(Creator)
admin.site.register(Store)
admin.site.register(MealPlanEntry)
