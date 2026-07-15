"""
URL configuration for the calorie_tracker application.
"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("edit/<int:pk>/", views.edit_food_item, name="edit_food_item"),
    path("delete/<int:pk>/", views.delete_food_item, name="delete_food_item"),
    path("reset/", views.reset_calories, name="reset_calories"),
]
