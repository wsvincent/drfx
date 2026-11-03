# DRFx

A framework for launching new Django Rest Framework projects quickly. Comes with a custom user model, login/logout/signup, social authentication via django-allauth and dj-rest-auth, and more.

## Features

- Django 6.1, Django REST Framework 3.18, and Python 3.12+
- Custom user model
- Token-based auth via [dj-rest-auth](https://github.com/iMerica/dj-rest-auth)
- Signup/login/logout
- [django-allauth](https://github.com/pennersr/django-allauth) for social auth
- [uv](https://docs.astral.sh/uv/) for dependency management (plain pip works too)

## First-time setup

1.  Make sure Python 3.12+ is installed. [See here for help](https://djangoforbeginners.com/initial-setup/).
2.  Clone the repo and install dependencies, using either uv (recommended) or pip.

With [uv](https://docs.astral.sh/uv/getting-started/installation/):

```
$ git clone https://github.com/wsvincent/drfx.git
$ cd drfx
$ uv sync
$ source .venv/bin/activate
```

Or with pip:

```
$ git clone https://github.com/wsvincent/drfx.git
$ cd drfx
$ python3 -m venv .venv
$ source .venv/bin/activate
(drfx) $ python -m pip install -r requirements.txt
```

On Windows, activate with `.venv\Scripts\activate` instead.

3.  Set up the initial migration for our custom user models in users and build the database.

```
(drfx) $ python manage.py makemigrations users
(drfx) $ python manage.py migrate
(drfx) $ python manage.py createsuperuser
(drfx) $ python manage.py runserver
```

4.  Endpoints

Login with your superuser account. Then navigate to all users. Logout. Sign up for a new account and repeat the login, users, logout flow.

- login - http://127.0.0.1:8000/api/v1/rest-auth/login/
- all users - http://127.0.0.1:8000/api/v1/users
- logout - http://127.0.0.1:8000/api/v1/rest-auth/logout/
- signup - http://127.0.0.1:8000/api/v1/rest-auth/registration/
