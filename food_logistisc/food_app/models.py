from django.db import models


class Ingredients(models.Model):
    GRAMME = 'g'
    ML = 'ml'
    measures = (
        (GRAMME, 'Gramme'),
        (ML, 'Milliliter'),
    )
    ingredient_name = models.CharField(max_length=30)
    ingredient_desc = models.CharField(max_length=200)
    ingredient_measure = models.CharField(
        max_length=2,
        choices=measures,
        default=GRAMME,
    )

    def __str__(self):
        return self.ingredient_name


class Compositions(models.Model):
    composition_name = models.CharField(max_length=50)
    ingredient = models.OneToOneField(Ingredients, on_delete=models.SET_NULL, null=True)
    ingredient_amount = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.composition_name


class Recipes(models.Model):
    recipe_name = models.CharField(max_length=50)
    recipe_desc = models.CharField(max_length=200)
    recipe_persons = models.PositiveIntegerField(default=1)
    compositions = models.ForeignKey(Compositions, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.recipe_name


class Dishes(models.Model):
    dish_name = models.CharField(max_length=50)
    dish_desc = models.CharField(max_length=200)
    dish_persons = models.PositiveIntegerField(default=1)
    dish_recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.dish_name
