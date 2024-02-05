# Marina Management System

## Introduction

Welcome to Marina, a demo web application designed to streamline marina operations by providing users with tools to manage boat registrations, licenses, and marina space reservations. 
Far from a fully functional, real-world application, this web application is merely reflective of my learning experiences with Django. 

## Database

The system uses an SQLite database, with the database schema defined in `marina/models.py`.

## Views

The views in `marina/views.py` handle various functionalities, including user authentication, boat registration, and marina space reservation.

## URLs

URL patterns and routing logic are defined in `marina/urls.py`. This dictates how different views are mapped to specific URLs.

## Forms

User input is managed through forms defined in `marina/forms.py`. These forms handle data validation and submission.

## Static Files

- **CSS Files**: Styles for different pages (e.g., boat, boatspaces, forms, index, login, profile).
- **Image Files**: Images used in the application (e.g., auth, home, profile, reservations).

## Templates


- **HTML Files**: Templates for different pages (e.g., add_boat, base, boatspace_list, edit_boatspace, index, license, login, profile, registration, signup, success).

## Installation and Setup

### Requirements

- [Pipenv](https://pipenv.pypa.io/en/latest/)

### Setup Instructions

1. Make sure you are in the Django-Marina directory in your terminal. 
2. Install dependencies using Pipenv:
   ```pipenv sync```
4. Activate the virtual environment:
   ```pipenv shell```
5. Run the development server:
   ```python3 manage.py runserver```
6. Visit the link provided and add '/marina' add the end of the URL. **Do not** forget this step, or you will get a 404 error. The URL should look something like: http://localhost:8000/marina
7. Explore!





