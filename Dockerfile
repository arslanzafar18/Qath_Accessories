From python:3
Run pip install django==3.2.12
Run pip install asgiref==3.5.0
Run pip install Pillow==9.0.1
Run pip install pytz==2021.3
Run pip install sqlparse==0.4.2
Run pip install django-crispy-forms==1.14.0
Run pip install typing-extensions==4.1.1


copy . .

Run python manage.py migrate
CMD ["python","manage.py","runserver","0.0.0.0:8001"]
