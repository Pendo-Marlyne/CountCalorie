"""
Models for the calorie_tracker application.

Defines the FoodItem model used to store food entries and their calorie counts.
"""

from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


class FoodItem(models.Model):
    """
    Represents a single food item consumed on a given day.

    Attributes:
        name: The name of the food item.
        calories: The number of calories in the food item.
        consumed_date: The date the food was consumed (used for daily tracking).
        created_at: Timestamp when the record was created.
    """

    name = models.CharField(max_length=200)
    calories = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Calorie count must be at least 1.",
    )
    consumed_date = models.DateField(default=timezone.localdate)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Food Item"
        verbose_name_plural = "Food Items"

    def __str__(self):
        return f"{self.name} ({self.calories} cal)"
