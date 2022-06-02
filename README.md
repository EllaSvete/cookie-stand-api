# api-quick-start

- Template Project for starting up CRUD API with Django Rest Framework

- [Ella's Deployed Cookie Stand](https://ellas-cookie-stand.herokuapp.com/api/v1/cookie_stand/)

## Customization Steps

- DO NOT migrate yet
- add additional dependencies as needed
  - Re-export requirements.txt as needed
- change `things` folder to the app name of your choice
- Search through entire code base for `Thing`,`Things` and `things` to modify code to use your resource
  - `project/settings.py`
  - `project/urls.py`
  - App's files
    - `views.py`
    - `urls.py`
    - `admin.py`
    - `serializers.py`
    - `permissions.py`
- Update ThingModel with fields you need
  - Make sure to update other modules that would be affected by Model customizations. E.g. serializers, tests, etc.
- Rename `project/.env.sample` to `.env` and update as needed
- Run makemigrations and migrate commands
- Optional: Update `api_tester.py`

## Step By Step Set Up

- Step 1: use template to make new repo
- Step 2: clone it down, cd into the repo
- Step 3: docker compose run web bash
- Step 4: python -c "import secrests: print(secrets.token_urlsafe())"
- Step 5:  exit
- Step 6: docker compose up
- Step 7:  Change App to App name you want
- Step 8: Go to settings.py and change all the "things" to the new app name (line 63)
- Step 9: Go to urls.py and change all the "things" to the new app name
- Step 10: Go to api_tester.py and change all the "thigns to new" app name
- Step 11: Go to views.py and change model name, serializer name and the class names from Thing to new App Name
- Step 12: Go to app urls.py and change the .views import and the path.as_views as well as the names from thing to new app name
- Step 13: tests change Thing to new app name
- Step 14: go to serializers.py and change the model import as well as the class name, and the model name in the class.
- Step 15: Go to apps.py and change Class name to AppConfig and name = name of app
- Step 16: in admin.py change the model inmport and the admin register site.
- Step 17: Go to models and update the model fields as necessary, make sure to adjust the str dunder method as needed. and update the class name.
- Step 18: docker compose run web bash
- Step 19: python manage.py showmigrations
    - Step 19.b: chase bugs as necessary
- Step 20: python manage.py makemigrations
- Step 21: python manage.py migrate
- Step 22: python manage.py createsuperuser
- Step 22.b: input super user name email and password
- Step 23: exit
- Step 24: docker compose up --build
- Step 24.b: check website. It work! Great!
- Step 25: register new instance on elephantsql
- Step 25.b: this will give you the information to put in your env file for the database
- Step 26: go to your env file add the "User and Default database" characters to your "DATABASE_NAME/USER" variables in the env file
- Step 27: Grab the password from the DB site and add to your "DATABASE_PASSWORD" variable in your env file
- Step 28: Server URL and add it to the "DATABASE_HOST" variable in your env file
- Step 29: docker compose run web bash
- Step 30: pip install psycopg2-binary
- Step 31: pip freeze > requirements.txt
- Step 32: exit
- Step 33: docker compose down *you must do a rebuild after changing the env file*
- Step 34: docker compose up --build
- Step 35: docker compose run web bash
- Step 36: python manage.py showmigrations
- Step 37: python manage.py migrate
- Step 38: python manage.py createsuperuser (again)
- Step 39: exit
- Step 40: docker compose up
- Step 41: login and create an object on your local host
- Step 42: Go back to ElephantSQL click on Browser on the left hand side, Select your isntance in the "Table queries" drop down menu, then click execute. Verify that your entry was registered to the database. Yes? Connected! Yay!
- Step 43: install heroku in your terminal if you havent and go through the process to login by typing in "heroku login"
- Step 44: open heroku in your browser and create a new app
- Step 45: in your new app navigate to the settings
- Step 46: reveal config vars
- Step 47: add EVERYTHING from your env file to your config vars
- Step 47.b: ALLOWED_HOSTS is going to be the heroku url you created for your app without the https:// and without the trailing /
- Step 48: heroku app:create appnameofyourchoosing
- Step 49: heroku stack:set container
- Step 50: In your settings.py file at the bottom of the file put this line of code:

```python
CSRF_TRUSTED_ORIGINS = [
    'https://yourapp.herokuapp.com'
]
```

- Step 51: rm db.sqlite3
- Step 52: git add .
- Step 53: git commit -m "heroku set up"
- Step 54: git push heroku main
- Step 55: python manage.py collectstatic
