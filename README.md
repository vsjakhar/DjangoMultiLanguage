# DjangoMultiLanguage
Django Multi Language

## Create Virtualenv with Python3 in Linux, Ubuntu or MAC
	virtualenv virtual/dml -p python3

## Create Virtualenv with Python3 in Windows
	python -m venv virtual\dml

## Activate Virtualenv in Linux, Ubuntu or MAC
	source virtual/dml/bin/activate

## Activate Virtualenv in Windows
	. virtual\dml\Scripts\activate

## Install Django and all Modules with pip3
	pip3 install django
	django-admin startproject MultiLanguage
	django-admin startproject MultiLanguage .
	pip3 install Pillow
	pip3 install django-ckeditor
	pip3 install django-extensions
	pip3 install djangorestframework
	pip3 install django-rest-auth
	pip3 install django-cors-headers
	pip3 install django-filter
	pip3 install fcm_django
	pip3 install xmltodict
	pip3 install mysqlclient
	pip3 install django-admin-sortable2
	pip3 install django-import-export
	pip3 install django-admin-autocomplete-filter
	pip3 install stripe
	LDFLAGS=-L/usr/local/opt/openssl/lib pip install mysqlclient

## Update requirements.txt file
	pip3 freeze > requirements.txt

## Install requirements.txt file
	pip3 install -r requirements.txt

## Start New Project in Django
	django-admin startproject clearamber

## Create New App in Django
	python manage.py startapp home
	python manage.py startapp blog
	python manage.py startapp jobs
	python manage.py startapp leads

## Run Django
	python manage.py runserver
	python manage.py runserver 8080
	python manage.py runserver 0:8000
	python manage.py runserver 192.168.1.4:8000

## Create Superuser
	python manage.py createsuperuser

## Reset user Password from Terminal
	python manage.py changepassword username

## Makemigrations of Project or Single App
	python manage.py makemigrations
	python manage.py makemigrations blog

## Migrate Project or Single App
	python manage.py migrate
	python manage.py migrate blog
	python manage.py migrate --fake
	python manage.py migrate blog --fake

## Run this command for different setting
	python3 manage.py runserver --settings=MultiLanguage.settings.local

## Run this command for permanant setting in Linux, Ubuntu or MAC
	export DJANGO_SETTINGS_MODULE=MultiLanguage.settings.local

## Run this command for permanant setting in Windows
	SET DJANGO_SETTINGS_MODULE=MultiLanguage.settings.local

## Run on Local System
	DJANGO_SETTINGS_MODULE=MultiLanguage.settings.local python manage.py runserver

## Run on Test Server
	DJANGO_SETTINGS_MODULE=MultiLanguage.settings.testing python manage.py runserver

## Run on Staging Server
	DJANGO_SETTINGS_MODULE=MultiLanguage.settings.staging python manage.py runserver

## Run on Circleci Server
	DJANGO_SETTINGS_MODULE=MultiLanguage.settings.circleci python manage.py runserver

## Run on Production Server
	DJANGO_SETTINGS_MODULE=MultiLanguage.settings.production python manage.py runserver

## Run on Production Server
	python manage.py runserver

## Static files on Production Server
	python manage.py collectstatic
	python manage.py collectstatic --noinput
	python manage.py collectstatic --noinput --clear

## Import and Export Database
	mysqldump -u clearamber -p operations_test > operations.sql
	mysql -u clearamber -p operations < operations.sql
	mysql -u clearamber -p deskisolate_testing < home/static/home_country.sql

## Install Memcached in MAC
	brew install memcached
	brew services start memcached

## Install Memcached in Ubuntu
	sudo apt-get install memcached
	sudo service memcached start

## Stripe Payment Gateway Integration
[Stripe Checkout page]('https://stripe.com/docs/payments/checkout')
[Stripe checkout One time redirect]('https://stripe.com/docs/payments/checkout/one-time#redirect-checkout')
[Stripe Success page data collection]('https://stripe.com/docs/payments/checkout/collecting')
[Stripe Payment confirmation]('https://stripe.com/docs/api/payment_intents/retrieve')

## Install and Setup Redis Channel Layer for Message sent and recive
Before install channels_redis we need to install Redis server with Docker or Direct on our server and run it before using
We will use a channel layer that uses Redis as its backing store. To start a Redis server with Docker on port 6379, run the following command:

	docker run -p 6379:6379 -d redis:2.8

For Mac you can Install and Start Redis by these Commands and also check redis info
	
	brew install redis
	brew services start redis
	brew info redis

For Ubuntu you can Install and Start Redis Server by these commands and also check redis info

	sudo apt install redis-server
	sudo systemctl status redis
	sudo systemctl restart redis.service

After Running Redis Server you can Install redis for Channels with This Command

	pip3 install channels_redis

# Heroku Setup

## Install the Heroku CLI
Download and install the Heroku CLI.

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

	$ heroku login

## Create Heroku Project
	heroku create MultiLanguage

## Add Heroku Setting a buildpack on an application
	heroku buildpacks:set heroku/python

## You may also specify a buildpack during app creation
	heroku create MultiLanguage --buildpack heroku/python

## Check Git Version and Initialize Git repo
	git --version
	git init

## Add Heroku settings in Current repo
	heroku git:remote -a MultiLanguage

## Configuring Django Apps for Heroku with 'Procfile' to add this code
	web: gunicorn MultiLanguage.wsgi

## Install gunicorn and django-heroku for Hosting
	pip3 install gunicorn
	pip3 install django-heroku

## Import django_heroku at top of Setting file and locals settings at Botton
	import django_heroku
	django_heroku.settings(locals())

## Follow this Link for More details
	https://devcenter.heroku.com/articles/django-app-configuration

## Set DJANGO_SETTINGS_MODULE env in wsgi file to heroku
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MultiLanguage.settings.heroku')

## Push and Deploy the code on Heroku
	pip3 freeze > requirements.txt
	git status
	git add .
	git commit -m "Project Initial Setup"
	git push heroku master

## If we got static files related error then we need to disable it
	heroku config:set DISABLE_COLLECTSTATIC=1

## Access Heroku Bash run migrations commands
	heroku run bash
	python3 manage.py migrate
	python3 manage.py createsuperuser

## Check Logs if we got any error
	heroku logs --tail

### Thanks for Reading... ###
# Happy Coading!!! #