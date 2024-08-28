# Edg.sh - URL Shortener

Edg.sh is a URL shortener built with Django.

## Setup

1. Clone the repo
2. Create a virtual environment (`python -m venv .venv`)
3. Install dependencies (`pip install -r requirements.txt`)
4. Create a database 
5. Set ENV variables
5. Run migrations (`python manage.py migrate`)
6. Create a superuser (`python manage.py createsuperuser`)
7. Run the server (`python manage.py runserver`)
8. Run the tailwind dev server (builds your tailwind styles `python manage.py tailwind start`)

### TODO

- [ ] Fix design
- [ ] Add more functionality like analytics, etc. on clicks

### Goals

This project is a basic URL shortener built with Django. I enjoy Python and Django, but I
barely get to use it, so I thought this would be a good way to use it more. Also I'm trying
to build and deploy more projects. I built a better one a while ago with GraphQL and Next.js [Here](https://github.com/zuice/edg.sh).
