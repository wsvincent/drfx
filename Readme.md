# DRFx

A framework for launching new Django Rest Framework projects quickly with a complete user authentication flow, custom user model, and social authentication options via Gmail, Facebook, Twitter, etc.

## Features

* Django 2.0 and Python 3.6
* Custom user model
* Email/password for login/signup
* User registration
* [django-allauth](https://github.com/pennersr/django-allauth) for easy social auth
* [Pipenv](https://github.com/pypa/pipenv) for virtualenvs

## First-time setup

1.  Make sure Python 3.6x and Pipenv are already installed. [See here for help](https://djangoforbeginners.com/initial-setup/).
2.  Clone the repo and configure the virtual environment:

```
$ git clone https://github.com/wsvincent/drfx.git
$ cd drfx
$ pipenv install
$ pipenv shell
```

3.  Set up the initial migration for our custom user models in users and build the database.

```
(drfx) $ python manage.py makemigrations users
(drfx) $ python manage.py migrate
Create a superuser:
(drfx) $ python manage.py createsuperuser
Confirm everything is working:
(drfx) $ python manage.py runserver
```

Load the site at http://127.0.0.1:8000.

6.  (Optional) Under "Sites" in the admin http://127.0.0.1:8000/admin/sites/site/ change "example.com" to "127.0.0.1" and the name to whatever your project is called, for example djangox.
