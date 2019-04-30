from django.contrib import admin
from .models import Ingredients, Recipes, Compositions, Dishes


@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('ingredient_name', 'ingredient_desc', 'ingredient_measure')
    fields = ('ingredient_name', 'ingredient_desc', 'ingredient_measure')


@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ('recipe_name', 'recipe_desc', 'recipe_persons')
    fields = ('recipe_name', 'recipe_desc', 'recipe_persons')


@admin.register(Compositions)
class CompositionsAdmin(admin.ModelAdmin):
    list_display = ('composition_name', 'recipe', 'ingredient', 'ingredient_amount')
    fields = ('composition_name', 'recipe', 'ingredient', 'ingredient_amount')


@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    list_display = ('dish_name', 'dish_desc', 'dish_persons', 'dish_recipe')
    fields = ('dish_name', 'dish_desc', 'dish_persons', 'dish_recipe')
