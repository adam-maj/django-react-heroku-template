# django-react-heroku-template
Boilerplate template for django-react app with heroku and heroku-postgres

# Heroku/Git Setup
1. Create a new heroku app on the [heroku dashboard](dashboard.heroku.com)
2. Add "heroku postgres" to the apps add-ons
3. Go to the deploy tab and select "GitHub" as the deployment method, then connect it to the intended repo
4. Go to settings and add both "heroku/nodejs" and "heroku/python" to the buildpacks. Make sure the nodejs buildpack comes first (otherwise django will try to collectstatic before react has run build).
5. Configure necessary environment variables. To get and setup a secret key, set the 'DJANGO_SECRET_KEY' environment variable to a key generated at this [django secret key generator](https://djecrety.ir/)
6. Go to deploy tab and click "deploy branch" in the manual deploy section
7. Delete the first two commands out of the release-tasks.sh and push the changes

# Django Backend Setup
1. Create models in models.py
2. Import and add serializers for all necessary models in serializers.py
3. Register all necessary models in admin.py
4. Import and create API endpoints for all necessary models in views.py
5. Configure url endpoints for all API endpoints in views.py

# Important Code in Repo
1. package.json, package-lock.json, and requirements.txt are all in the root directory. Heroku will automatically look for these files there to install the dependencies.
2. Procfile runs the Django wsgi file with gunicorn
3. React app "src" and "public" folders are in the root directory (not inside another react app folder)
4. Static files directory is configured in "TEMPLATES" setting on settings.py
5. Django heroku called on last line of settings file configures databse, allowed hosts, etc. ([django_heroku documentation](https://pypi.org/project/django-heroku/))
6. The release tasks specifically migrates api because there is no migrations folder there
7. Everytime a heroku dyno is destroyed, it loses all memory of past migrations and is very easy to break

# Change App Name
1. Change name of appname folder
2. Change any instance of "appname" to your project name in the following areas (use CTRL or CMD + F to find):
    1. appname/asgi.py (Line 14)
    2. appname/wsgi.py (Line 14)
    3. appname/settings.py (Line 54, Line 72)