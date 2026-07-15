"""
Views for the calorie_tracker application.

Handles CRUD operations for food items, daily calorie totals, and reset functionality.
"""

from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from .forms import FoodItemForm
from .models import FoodItem


def get_today_food_items():
    """Return all food items consumed today, ordered by most recent."""
    today = timezone.localdate()
    return FoodItem.objects.filter(consumed_date=today)


def calculate_total_calories(food_items):
    """Calculate the total calories from a queryset of food items."""
    result = food_items.aggregate(total=Sum("calories"))
    return result["total"] or 0


def index(request):
    """
    Display today's food items, total calories, and the add-food form.

    Supports creating new food items via POST request.
    """
    food_items = get_today_food_items()
    total_calories = calculate_total_calories(food_items)

    if request.method == "POST":
        form = FoodItemForm(request.POST)
        if form.is_valid():
            food_item = form.save(commit=False)
            food_item.consumed_date = timezone.localdate()
            food_item.save()
            messages.success(request, f"Added {food_item.name} ({food_item.calories} cal).")
            return redirect("index")
        messages.error(request, "Please correct the errors below.")
    else:
        form = FoodItemForm()

    context = {
        "food_items": food_items,
        "total_calories": total_calories,
        "form": form,
        "today": timezone.localdate(),
    }
    return render(request, "calorie_tracker/index.html", context)


def edit_food_item(request, pk):
    """Update an existing food item."""
    food_item = get_object_or_404(FoodItem, pk=pk, consumed_date=timezone.localdate())

    if request.method == "POST":
        form = FoodItemForm(request.POST, instance=food_item)
        if form.is_valid():
            form.save()
            messages.success(request, f"Updated {food_item.name}.")
            return redirect("index")
        messages.error(request, "Please correct the errors below.")
    else:
        form = FoodItemForm(instance=food_item)

    return render(request, "calorie_tracker/edit.html", {"form": form, "food_item": food_item})


@require_POST
def delete_food_item(request, pk):
    """Remove a food item from today's list."""
    food_item = get_object_or_404(FoodItem, pk=pk, consumed_date=timezone.localdate())
    name = food_item.name
    food_item.delete()
    messages.success(request, f"Removed {name} from today's list.")
    return redirect("index")


@require_POST
def reset_calories(request):
    """Clear all food items for the current day."""
    today = timezone.localdate()
    deleted_count, _ = FoodItem.objects.filter(consumed_date=today).delete()
    if deleted_count:
        messages.success(request, "Today's calorie count has been reset.")
    else:
        messages.info(request, "No food items to reset for today.")
    return redirect("index")
