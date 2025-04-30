# WorkingHorse

A comprehensive web application for horse owners and trainers to manage horses, track race performances, and monitor expenses.

## Description

WorkingHorse is a Django-based application that helps equestrians keep detailed records of their horses including acquisition details, racing history, and all associated expenses. The app allows users to track horse performance, manage financial aspects, and make data-driven decisions about their equine business or hobby.

## Features

### Horse Management
- **Add Horses**: Record new horses with details such as name, acquisition date, purchase price, type, and location
- **View Horses**: See all active horses in your collection
- **Edit Horse Details**: Update information as needed
- **Sell Horses**: Mark horses as sold and record selling prices
- **Track Sold Horses**: Separate view for horses that have been sold

### Race Tracking
- **Record Races**: Log race performances including earnings, dates, finishing positions, and race types
- **Filter Races**: Search and filter race history by date ranges and race types
- **Edit Race Details**: Update race information as needed

### Expense Management
- **Track Expenses**: Record all horse-related expenses with detailed categorization
- **Expense Categories**: Organize expenses into predefined categories:
  - Veterinary Care
  - Feed & Nutrition
  - Training & Lessons
  - Boarding & Stabling
  - Equipment & Tack
  - Farrier & Hoof Care
  - Transportation
  - Competition & Race Fees
  - Insurance
  - Other Expenses
- **Filter Expenses**: Search and organize expenses by various criteria

## Technologies Used

- **Backend**: Django 4.0.6
- **Database**: SQLite (default)
- **Filtering**: django-filter 22.1
- **Frontend**: Bootstrap (for styling and UI components)
- **Authentication**: Django's built-in authentication system

## Installation and Setup

1. **Clone the repository**
   ```
   git clone <repository-url>
   cd WorkingHorse
   ```

2. **Create and activate a virtual environment**
   ```
   python -m venv env
   # On Windows
   env\Scripts\activate
   # On macOS/Linux
   source env/bin/activate
   ```

3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```
   python manage.py migrate
   ```

5. **Create a superuser (admin)**
   ```
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000/`
   - Access the admin interface at `http://127.0.0.1:8000/admin/`

## Usage Guide

### Getting Started
1. Register for an account or log in
2. Add your horses to the database
3. Begin tracking races and expenses

### Horse Management
- Navigate to "Your Horses" to view all active horses
- Use the "Add Horse" button to register new horses
- Click on a horse's name to view its details
- Use the "Edit" button to update horse information
- Use the "Sell" button to mark a horse as sold and record the selling price

### Race Tracking
- Navigate to the Races section
- Use the "Add Race" button to record new race performances
- Use the date filters to search for races within specific time periods
- Use the type filter to find races of a specific category

### Expense Management
- Navigate to the Expenses section
- Use the "Add Expense" button to record new expenses
- Select the appropriate category for each expense
- Associate expenses with specific horses
- Use the filters to analyze expenses by various criteria

## Authentication

The application uses Django's built-in authentication system:
- User registration with username and password
- Secure login/logout functionality
- User-specific data - each user can only see and manage their own horses, races, and expenses
- Password reset capabilities

## Deployment

The application is configured to be deployed on Heroku, but can be deployed on any platform that supports Django applications.

## License

MIT License

Copyright (c) 2025 WorkingHorse

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
