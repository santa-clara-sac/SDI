@echo off
cd /d C:\Users\Administrador\Desktop\temp
call .venv\Scripts\activate
python manage.py runserver 0.0.0.0:8000