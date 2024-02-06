# Django Todo App

## Introduction

This project is a simple Todo application built with Django. It allows users to add, update, and delete todo items. This app demonstrates the fundamental concepts of Django, including models, views, forms, and templates.

## Features

- Add todo items
- Update the completion status of todo items
- Delete todo items

## Setup and Installation

### Requirements

- Python 3.x
- Django

### Creating a Virtual Environment

To isolate the project dependencies, it's recommended to create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Unix or MacOS
.\venv\Scripts\activate  # On Windows
```

### Installing Dependencies

Install Django and other necessary packages from the requirements.txt file:

```
pip install -r requirements.txt
```

### Database Migrations

Before running the application, apply the migrations to set up your database schema:

```
python manage.py makemigrations
python manage.py migrate
```

## Running the Application

Start the Django development server:

```
python manage.py runserver
```

Access the application by navigating to http://127.0.0.1:8000/ in your web browser.
