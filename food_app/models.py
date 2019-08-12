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

    # def __str__(self):
    #     return 'Ингредиенты для {}'.format(self.recipe_id)


class Dish(models.Model):
    dish_name = models.CharField(max_length=50)
    dish_recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.dish_name


class Day2Meal(models.Model):
    date = models.DateField()


class Meal(models.Model):
    persons = models.PositiveIntegerField(default=1)
    meal_dish = models.ForeignKey(Dish, on_delete=models.SET_NULL, null=True)
    meal_date = models.ForeignKey(Day2Meal, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{}'.format(self.meal_dish)
