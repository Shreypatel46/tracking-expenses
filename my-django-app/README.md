# Django Expense Tracker

A simple and beautiful expense tracking web application built with Django.

## Features

- **Add Expenses**: Track your expenses with category, amount, description, and date
- **Category Breakdown**: View total expenses broken down by category
- **Beautiful UI**: Modern, responsive design with a piggy bank theme
- **Admin Interface**: Manage expenses through Django admin panel
- **Real-time Totals**: See your total expenses and category-wise spending

## Categories

The application supports the following expense categories:
- Food
- Transportation
- Entertainment
- Utilities
- Shopping
- Healthcare
- Education
- Other

## Installation & Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create Superuser** (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

4. **Start Development Server**:
   ```bash
   python manage.py runserver
   ```

5. **Access the Application**:
   - Main application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Usage

1. **Adding Expenses**: Fill out the form on the main page with:
   - Category (dropdown selection)
   - Amount (in dollars)
   - Description (what you spent on)
   - Date (defaults to today)

2. **Viewing Expenses**: The main page shows:
   - Total expenses across all categories
   - Breakdown by category
   - List of recent expenses with delete option

3. **Managing Expenses**: Use the admin panel to:
   - View all expenses
   - Edit expense details
   - Delete expenses
   - Filter by category or date

## Project Structure

```
my-django-app/
├── expenses/                 # Main app
│   ├── models.py            # Expense model
│   ├── views.py             # View functions
│   ├── urls.py              # URL patterns
│   ├── admin.py             # Admin configuration
│   ├── templates/           # HTML templates
│   │   └── expenses/
│   │       └── index.html   # Main template
│   └── static/              # Static files
│       └── expenses/
│           ├── style.css    # CSS styling
│           └── piggy-bank.svg # Logo image
├── mytracker/               # Project settings
│   ├── settings.py          # Django settings
│   └── urls.py              # Main URL configuration
├── manage.py                # Django management script
└── requirements.txt         # Python dependencies
```

## Technologies Used

- **Backend**: Django 4.2.7
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (default)
- **Styling**: Custom CSS with modern design principles

## Default Admin Credentials

- Username: `admin`
- Password: Set during superuser creation

Enjoy tracking your expenses! 🐷💰
