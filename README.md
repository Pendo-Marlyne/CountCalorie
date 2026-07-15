# Calorie Counter

A Django web application for tracking daily calorie intake. Add food items, view your daily list, calculate total calories consumed, and reset your count at the end of the day.

**Live Demo:** [https://countcalorie.onrender.com](https://countcalorie.onrender.com) *(update this URL after deploying to Render)*

## Features

- **Add food items** with name and calorie count
- **View all food items** consumed today in a responsive list
- **Edit and remove** individual food items
- **Calculate total calories** consumed for the current day
- **Reset daily count** to clear all items for today
- **Responsive UI** built with Tailwind CSS
- **PostgreSQL database** for persistent storage

## Tech Stack

- Python 3.x
- Django 6.x
- PostgreSQL
- HTML5 / CSS3
- Tailwind CSS (via CDN)
- Git for version control

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

- Python 3.10+
- PostgreSQL installed and running
- Git

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd countcalorie
```

### 2. Create and activate a virtual environment

```bash
python -m venv myenv

# Windows
myenv\Scripts\activate

# macOS/Linux
source myenv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example environment file and update values for your local PostgreSQL instance:

```bash
cp .env.example .env
```

Set these variables (or export them in your shell):

| Variable      | Description              | Default              |
|---------------|--------------------------|----------------------|
| `SECRET_KEY`  | Django secret key        | (required in prod)   |
| `DEBUG`       | Debug mode               | `True`               |
| `DB_NAME`     | PostgreSQL database name | `calorie_counter_db` |
| `DB_USER`     | PostgreSQL username      | `postgres`           |
| `DB_PASSWORD` | PostgreSQL password      | `postgres`           |
| `DB_HOST`     | Database host            | `localhost`          |
| `DB_PORT`     | Database port            | `5432`               |

### 5. Create the PostgreSQL database

```sql
CREATE DATABASE calorie_counter_db;
```

### 6. Run migrations

```bash
cd countcalorie
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## Usage

1. **Add a food item** — Enter the food name and calorie count, then click "Add to Today's List".
2. **View your list** — All items added today appear in the Food Items panel with timestamps.
3. **Edit an item** — Click the pencil icon to update name or calories.
4. **Remove an item** — Click the trash icon to delete a single food item.
5. **Check total calories** — The total is displayed prominently at the top of the page.
6. **Reset the day** — Click "Reset Day" to clear all food items for today.

## Deployment to Render

### 1. Push code to GitHub

```bash
git init
git add .
git commit -m "Initial commit: Calorie Counter Django app"
git remote add origin <your-github-repo-url>
git push -u origin main
```

### 2. Create a PostgreSQL database on Render

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **New +** → **PostgreSQL**
3. Name it (e.g., `calorie-counter-db`) and create it
4. Copy the **Internal Database URL**

### 3. Create a Web Service on Render

1. Click **New +** → **Web Service**
2. Connect your GitHub repository
3. Configure:
   - **Environment:** Python 3
   - **Build Command:** `./build.sh`
   - **Start Command:** `cd countcalorie && gunicorn countcalorie.wsgi`
4. Add environment variables:
   - `SECRET_KEY` — generate a secure random key
   - `DEBUG` — `False`
   - `ALLOWED_HOSTS` — `your-app-name.onrender.com`
   - `DATABASE_URL` — paste the Internal Database URL from step 2
5. Click **Create Web Service**

### 4. Update README

After deployment, replace the live demo URL at the top of this README with your Render app URL.

## Security

- CSRF protection enabled on all forms
- POST-only endpoints for delete and reset actions
- Environment variables used for secrets (never committed to Git)
- Production security headers enabled when `DEBUG=False`
- Input validation on calorie counts (minimum value of 1)

## License

This project is for educational purposes.
# CountCalorie
