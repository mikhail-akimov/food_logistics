from django.shortcuts import render
from rest_framework import viewsets
from .models import Day2Meal
from .serializers import DaySerializer
from django.http import JsonResponse
from rest_framework.decorators import action, api_view

# Create your views here.


class DayViewSet(viewsets.ModelViewSet):
    queryset = Day2Meal.objects.all()
    serializer_class = DaySerializer


