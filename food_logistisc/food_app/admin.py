from django.contrib import admin
from .models import (
    Ingredient,
    Measure,
    Recipe,
    Recipe2Ingredient,
    Dish,
    Meal,
    Meal2Dish,
    Day2Meal,
)


class MealsInline(admin.StackedInline):
    model = Meal
    extra = 0
    fields = [('meal_dish', 'persons')]


class Recipe2IngredientsInline(admin.StackedInline):
    model = Recipe2Ingredient
    extra = 0
    verbose_name = 'Ingredient'
    fields = [('ingredient_id', 'value', 'measure_id')]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('ingredient_name',)


@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):
    list_display = ('measure_name',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe_name', 'recipe_description', 'default_persons')
    inlines = [Recipe2IngredientsInline]


@admin.register(Recipe2Ingredient)
class Recipe2IngredientsAdmin(admin.ModelAdmin):
    list_display = ('recipe_id', 'ingredient_id', 'value', 'measure_id')


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('dish_name', 'dish_recipe')


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('meal_dish', 'persons')
    fields = ('meal_dish', 'persons')


@admin.register(Meal2Dish)
class Meal2DishAdmin(admin.ModelAdmin):
    list_display = ('dish_id', 'meal_id')


@admin.register(Day2Meal)
class Day2MealAdmin(admin.ModelAdmin):
    list_display = ('date', )
    inlines = [MealsInline]


