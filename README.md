# Calorie Counter
A Django web application for tracking daily calorie intake. Add food items, view your daily list, calculate total calories consumed and reset your count at the end of the day.

**Live Demo:** 
[https://count-calorie-website.onrender.com]

## Features
- *Add food items* with name and calorie count
- *View all food items* consumed today in a responsive list
- *Edit and remove*individual food items
- *Calculate total calories* consumed for the current day
- *Reset daily count* to clear all items for today
- *Responsive UI* built with Tailwind CSS
- *PostgreSQL database* for persistent storage

## Tech Stack
- Python 
- Django 
- PostgreSQL
- HTML5 / CSS3
- Tailwind CSS (via CDN)

## Project Structure
```
countcalorie/
├── countcalorie/              # Django project settings
│   ├── calorie_tracker/       # Main app (models, views, templates)
│   ├── countcalorie/          # Project configuration
│   └── manage.py
├── requirements.txt
├── Procfile                   # Render deployment
├── build.sh                   # Render build script
├── .env.example               # Environment variable template
└── README.md
```

## Local Setup

### Prerequisites
- Python 3
- PostgreSQL installed and running
- Git

## Usage
1. *Add a food item* — Enter the food name and calorie count, then click "Add to Today's List".
2. *View your list* — All items added today appear in the Food Items panel with timestamps.
3. *Edit an item* — Click the pencil icon to update name or calories.
4. *Remove an item* — Click the trash icon to delete a single food item.
5. *Check total calories*— The total is displayed prominently at the top of the page.
6. *Reset the day* — Click "Reset Day" to clear all food items for today.

## License

This project is for educational purposes.
# CountCalorie
