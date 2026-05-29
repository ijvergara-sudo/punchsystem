<<<<<<< HEAD
# Django Punch System

A simple employee attendance punch system using Django.

## Features

- Username + PIN punch
- Employee full name stored on each punch
- Punch IN / OUT automatically
- Employee recent punch report after punching
- Admin dashboard
- Admin-only live punch monitor at `/live/`
- CSS styling
- Render-ready deployment files

## Local setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations attendance
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:

- Punch page: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
- Reports: http://127.0.0.1:8000/reports/
- Live monitor: http://127.0.0.1:8000/live/

## Create employee

In Django admin, add an Employee:

- Username: john
- Full name: John Smith
- PIN: 1234
- Active: checked

Then punch using username `john` and PIN `1234`.
=======
# punchsystem
A punch system
>>>>>>> b673fa0a2f578d336e17974dd3669d014a1c67e7
