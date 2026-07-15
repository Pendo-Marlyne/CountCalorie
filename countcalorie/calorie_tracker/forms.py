"""
Forms for the calorie_tracker application.

Provides validated forms for creating and updating food items.
"""

from django import forms

from .models import FoodItem


class FoodItemForm(forms.ModelForm):
    """Form for adding or editing a food item."""

    class Meta:
        model = FoodItem
        fields = ["name", "calories"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": (
                        "w-full px-4 py-2 border border-gray-300 rounded-lg "
                        "focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 "
                        "outline-none transition"
                    ),
                    "placeholder": "e.g. Grilled Chicken Salad",
                }
            ),
            "calories": forms.NumberInput(
                attrs={
                    "class": (
                        "w-full px-4 py-2 border border-gray-300 rounded-lg "
                        "focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 "
                        "outline-none transition"
                    ),
                    "placeholder": "e.g. 350",
                    "min": "1",
                }
            ),
        }

    def clean_calories(self):
        """Ensure calorie count is a positive integer."""
        calories = self.cleaned_data.get("calories")
        if calories is not None and calories < 1:
            raise forms.ValidationError("Calories must be at least 1.")
        return calories
