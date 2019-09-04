from django.db import models


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=30)

    def __str__(self):
        return self.ingredient_name


class Measure(models.Model):
    measure_name = models.CharField(max_length=20)

    def __str__(self):
        return self.measure_name


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50, null=True)
    recipe_description = models.CharField(max_length=300)
    default_persons = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.recipe_name


class Recipe2Ingredient(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=False)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.PROTECT, null=False)
    value = models.PositiveIntegerField(default=1)
    measure_id = models.ForeignKey(Measure, on_delete=models.PROTECT, null=False)


class Dish(models.Model):
    dish_name = models.CharField(max_length=50)
    dish_recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.dish_name


class Day2Meal(models.Model):
    date = models.DateField()

    def get_all_meals(self):
        meals = list(Meal.objects.all().filter(meal_date=self))
        day_meals = {}
        for meal in meals:
            day_meals[str(meal)] = {'persons': int(meal.persons)}
        return day_meals

    def get_all_ingredients(self):
        meals = list(Meal.objects.all().filter(meal_date=self))
        measures = {}
        ing_mapping = {}
        menu = {}
        for meal in meals:
            ingredients = Recipe2Ingredient.objects.all().filter(recipe_id=meal.meal_dish.dish_recipe.pk)
            recipe_persons = Recipe.objects.get(pk=meal.meal_dish.dish_recipe.pk).default_persons
            meal_persons = meal.persons
            for ing in ingredients:
                ing_mapping[str(ing.ingredient_id)] = int(ing.id)
                measures[str(ing.ingredient_id)] = str(ing.measure_id)
                if menu.get(str(ing.ingredient_id)):
                    menu[str(ing.ingredient_id)] += (ing.value / recipe_persons) * meal_persons
                else:
                    menu[str(ing.ingredient_id)] = (ing.value / recipe_persons) * meal_persons
        for product in menu.keys():
            menu[str(product)] = {'id': int(ing_mapping[product]),
                            'value': menu[product],
                            'measure': measures[product]}
        return menu


class Meal(models.Model):
    persons = models.PositiveIntegerField(default=1)
    meal_dish = models.ForeignKey(Dish, on_delete=models.SET_NULL, null=True)
    meal_date = models.ForeignKey(Day2Meal, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{}'.format(self.meal_dish)

    def to_ingredients(self):
        ingredients = Recipe2Ingredient.objects.all().filter(recipe_id=self.meal_dish.dish_recipe.pk)
        result = []
        for item in ingredients:
            result.append({'ing': item.ingredient_id, 'value': item.value, 'measure': item.measure_id})
        return '{}'.format(ingredients)
