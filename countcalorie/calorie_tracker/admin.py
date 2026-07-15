"""
Admin configuration for the calorie_tracker application.
"""

from django.contrib import admin

from .models import FoodItem


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    """Admin interface for managing food items."""

    list_display = ("name", "calories", "consumed_date", "created_at")
    list_filter = ("consumed_date",)
    search_fields = ("name",)
    ordering = ("-consumed_date", "-created_at")
