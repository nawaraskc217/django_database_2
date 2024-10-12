django-admin startproject mysite
cd mysite
python manage.py startapp food
python manage.py startapp food
python manage.py runserver
python manage.py migrate


What Migrations Do
When you make changes to your Django models (like adding a new field, renaming a field, or changing field options), migrations allow you to:

Apply those changes to the database schema without manually writing SQL.
Ensure the database reflects the current structure of your Django models.
Version control database schema changes, making it easier to track and undo changes if needed.