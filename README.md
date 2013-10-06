django-snippets
===============

Django Snippets | This project was started for the purpose of learning Django

To setup project (temporary):

1. install virtualenv
2. install virtualenvwrapper
3. And run commands below:
    - pip install -r requirements/development.txt
    - export DJANGO_SETTINGS_MODULE=django_snippets.settings
    - python manage.py runserver_plus --settings=django_snippets.settings.local
    - python manage.py syncdb --settings=django_snippets.settings.local
    - python manage.py migrate --settings=django_snippets.settings.local
