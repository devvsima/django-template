# How to start?
This template has an initial user model and a small registration and login script. You can change it for yourself. 

### ~Venv
```bash
$ python -m venv .venv
$ python .venv/Scripts/activate
```

### ~Requirements
```bash
$ pip install -r requirements.txt
```

### ~Migrations
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

### ~Create admin
```bash
$ python manage.py createsuperuser
```

### ~Launch
```bash
$ python manage.py runserver
# or
$ python manage.py runserver 0.0.0.0:8000
```
