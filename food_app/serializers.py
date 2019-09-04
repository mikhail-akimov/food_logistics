from .models import Day2Meal, Meal
from rest_framework import serializers


class DaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Day2Meal
        fields = ['id', 'date', 'get_all_meals', 'get_all_ingredients']
