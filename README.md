# Django Todo App

A simple and clean todo application built with Django 5.2.3 that allows users to manage their daily tasks efficiently.

## Features

- Add new todo items with title and description
- Mark tasks as complete/incomplete
- Edit existing tasks
- Delete tasks

## Tech Stack

- **Backend**: Django 5.2.3
- **Database**: SQLite (default)
- **Frontend**: HTML templates with Django template engine
- **Python**: 3.x

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd todoproject
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Django**
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main app: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/
