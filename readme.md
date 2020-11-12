# Help wymco with his page

This project was created to help the reddit user wymco with his webpage. It can be used as a template for new webpages.

## Feauters

- Responsive and modern design
- Four static pages to present your company
- A blog where you can write articles and visiters can leave comments
- Admin menu where you can add and edit articles and approve comments

A demo page can be seen here: https://wymco.herokuapp.com/

Bear in mind the demo runs on a free heroku dyno. It can be slow on the first page load because the dyno goes to sleep afther some time of incativity,

## Set up developement environment
You need to have docker installed on your system.

1. Download this repository
2. cd into the projects root directory
3. create a .env file in the root directory
4. add the following environment variables to the file

```shell
DJANGO_SECRET_KEY=Just_some_random_text
DJANGO_ALLOWED_HOSTS=*
DJANGO_DEBUG=True
POSTGRES_PASSWORD=password
POSTGRES_USER=postgres
```
5. Build and run the containers

```shell
docker-compose build
docker-compose up
```

6. make migrations and create superuser

```shell
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

7. test if everything works correctly

```shell
docker-compose exec web python manage.py test
```

## Deploy
This project is ready to be deployed to heroku. Follow the steps below to deploy your own version. You first have to install the heroku cli.

1. Login and create your app

```shell
heroku login
heroku create <app_name>
heroku stack:set container --app=<app_name>
```

2. Connect your app with your git repository

```shell
heroku git:remote -a <app_name>
git checkout deploy
git push heroku deploy:master
```

3. Afther the image is build run the following commands:

```shell
heroku run python manage.py makemigrations
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```
4. Your app is now online here: https://<app_name>.herokuapp.com/
