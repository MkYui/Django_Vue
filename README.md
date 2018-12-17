This repo is a demo of django and vue.

## How to use

First, clone the repo and install the dependencies.

```bash
$ https://github.com/Caoyiii/django-vue-blog.git
# django dependencies.
$ cd django-vue-blog/backend/
$ pip install -r requirements.txt
# vue dependencies.
$ cd ../frontend/
$ npm i
```
Then, run it.
```bash
# in frontend
$ npm run dev
# in backend
$ python manage.py makemigrations Blog BlogUser
$ python manage.py migrate
# creating an admin user
$ python createsuperuser
...
$ python manage.py runserver
```

Now, open a Web browser and go to "http://localhost:8000/admin/" create posts.

go to "http://localhost:8080/#/" view.
