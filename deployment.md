Django Rest API Deployment Cheat Sheet

1	PostgresSQL – Elephan Sql
2	Create Heroku app
3	Config vars
4	Migrating your data.
a.	Install dj_database_url and psycopg2
pip3 install dj_database_url==0.5.0 psycopg2
b.	import dj_database_url underneath the import for os

import os
 import dj_database_url
c.	Update the DATABASES section

if 'DEV' in os.environ:
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': BASE_DIR / 'db.sqlite3',
         }
     }
 else:
     DATABASES = {
         'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
     }

This will ensure that when you have an environment variable for DEV in your environment the code will connect to the sqlite database here in your IDE. Otherwise it will connect to your external database, provided the DATABASE_URL environment variable exist.

2.	Update env.py
a.	os.environ['DATABASE_URL']
b.	os.environ['CLOUDINARY_URL'] = "cloudinary://..."
c.	 os.environ['SECRET_KEY'] = "Z7o..."
d.	 # os.environ['DEV'] = '1'
e.	 os.environ['DATABASE_URL'] = "postgres://..."
5	External database connection
a.	Bug print for

 

b.	-–dry-run your makemigrations
python3 manage.py makemigrations --dry-run

c.	Check the print statement
 

d.	Remove the print statement
e.	Run the migration
f.	Create superuser 
python3 manage.py createsuperuser
g.	Check the browser in ElephantSQL, run a “user auth query”
6	Prepare your code for deployment
i.	guniconrn and cors (cross origin resource sharing)
-	https://docs.gunicorn.org/en/stable/install.html 
-	https://github.com/adamchainz/django-cors-headers 
pip3 install gunicorn django-cors-headers


ii.	Update requirements.txt file
pip freeze --local > requirements.txt

iii.	Procfile

release: python manage.py makemigrations && python manage.py migrate
 web: gunicorn drf_api.wsgi
iv.	Update Allowed hosts

ALLOWED_HOSTS = ['localhost', '<your_app_name>.herokuapp.com']

v.	Add corsheaders to INSTALLED_APPS
INSTALLED_APPS = [
    ...
    'dj_rest_auth.registration',
    'corsheaders',
    ...
 ]
vi.	Add corsheaders middleware to the TOP of the MIDDLEWARE
SITE_ID = 1
 MIDDLEWARE = [
     'corsheaders.middleware.CorsMiddleware',
     ...
 ]

vii.	Under the MIDDLEWARE list, set the ALLOWED_ORIGINS for the network requests made to the server with the following code
if 'CLIENT_ORIGIN' in os.environ:
     CORS_ALLOWED_ORIGINS = [
         os.environ.get('CLIENT_ORIGIN')
     ]
 else:
     CORS_ALLOWED_ORIGIN_REGEXES = [
         r"^https://.*\.gitpod\.io$",
     ]
viii.	To be able to have the front end app and the API deployed to different platforms, set the JWT_AUTH_SAMESITE attribute to 'None'. Without this the cookies would be blocked
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None'
ix.	Remove the value for SECRET_KEY and replace with the following code to use an environment variable instead

 # SECURITY WARNING: keep the secret key used in production secret!
 SECRET_KEY = os.getenv('SECRET_KEY')
    
x.	Set a NEW value for your SECRET_KEY environment variable in env.py, do NOT use the same one that has been published to GitHub in your commits

 os.environ.setdefault("SECRET_KEY", "CreateANEWRandomValueHere")
xi.	Set the DEBUG value to be True only if the DEV environment variable exists. This will mean it is True in development, and False in production

 DEBUG = 'DEV' in os.environ
xii.	Comment DEV back in env.py

 import os

 os.environ['CLOUDINARY_URL'] = "cloudinary://..."
 os.environ['SECRET_KEY'] = "Z7o..."
 os.environ['DEV'] = '1'
 os.environ['DATABASE_URL'] = "postgres://..."
xiii.	Ensure the project requirements.txt file is up to date. In the IDE terminal of your DRF API project enter the following

 pip freeze --local > requirements.txt
7	Add, commit and push your code to GitHub

