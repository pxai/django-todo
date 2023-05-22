# Django 4 Todo
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/pxai/django-todo/tree/master.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/pxai/django-todo/tree/master)

# Setup venv

Create
```shell
python -m venv django-adboard
```

Enter
```shell
source django-adboard/bin/activate
```

Exit
```shell
deactivate
```

# Set up Django
Check out:

https://docs.djangoproject.com/en/4.1/intro/tutorial01/

Install stuff with:
```shell
 pip3 install Django~=4.1.0
 pip3 install coverage==3.6
```

Create a project
```shell
django-admin startproject adboard
```

Migrate db
```shell
python manage.py migrate
```

Add app (inside project):
```shell
python manage.py startapp adboardapp
```

RUN it!:
```shell
python manage.py runserver
```
or

```shell
python manage.py runserver 127.0.0.1:8001 --settings
```

## Running tests
You can just write all of them inside `adboardapp/tests.py`
But it's better to organize them inside `adboardapp/tests/other_test.py` and
`adboardapp/tests/models/other_test.py`.
Remove `adboardapp/tests.py` to avoid errors.

```shell
python manage.py test --noinput animals.tests
```

Assert reference
https://docs.python.org/3/library/unittest.html#assert-methods

## DB

```shell
python manage.py makemigrations appname
```
Dale:

```shell
python manage.py makemigrations adboardapp
```

Check it:

```shell
python manage.py sqlmigrate adboardapp 0001
```

Run it!!!

```shell
python manage.py migrate
```

## Testing

```shell
python manage.py test
```

Run coverage
```shell
coverage run manage.py test whatever -v 2
```

### Create fixtures

```shell
python manage.py dumpdata todoapp.Todo --pk 1 --indent 4 >> fixtures.json
```

```shell
python manage.py loaddata group.json
```

or in the test file
```python
    fixtures = ["group.json"]
```

## Query Sets
```python
python manage.py shell
>>> from django.contrib.auth.models import User
>>> from adboardapp.models import Ad
>>> Ad.objects.all()
>>> Ad.objects.all().count()
>>> Ad.objects.get(title='Whatever')
>>> ad = Ad(title='sdfa', author= User.objects.last())
>>> ad.save()
>>> ad.title = 'Changed title'
>>> ad.save()
>>> ad.delete()
>>> Ad.objects.filter(status='PUBLISHED').order_by('created_at').order_by('-title').filte(author__username='admin')
>>> Ad.objects.filter(title__startswith='New ad')

>>> Ad.objects.filter(status='PUBLISHED').exclude(id=1)

```

## Admin app
```shell
python manage.py createsuperuser
```

Then:

```shell
python manage.py runserver
```

Add models to admin. Edit `admin.py`

```python
admin.site.register(Ad)
```


http://127.0.0.1:8000/admin/

## Django shell
```shell
python manage.py shell
...
>>> from adboardapp.models import Ad
```


## Debug mode
Edit `settings.py`:

```shell
DEBUG=True
```

# requirements
Install stuff with:
```shell
pip3 install Django~=4.1.0
```

Save stuff
```shell
pip3 freeze > requirements.txt
```

Reuse it
```shell
pip3 install -r requirements.txt
```