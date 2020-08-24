# django-react-heroku-template
Boilerplate template for django-react app with heroku and heroku-postgres

# Heroku/Git Setup
1. Create a new heroku app on the [heroku dashboard](dashboard.heroku.com)
2. Add "heroku postgres" to the apps add-ons
3. Go to the deploy tab and select "GitHub" as the deployment method, then connect it to the intended repo
4. Go to settings and add both "heroku/python" and "heroku/nodejs" to the buildpacks
5. Configure necessary environment variables. To get and setup a secret key, set the 'DJANGO_SECRET_KEY' environment variable to the output of the following command: `python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
6. Go to deploy tab and click "deploy branch" in the manual deploy section
7. Click "enable automatic deploys" in the automatic deploys section

# Important Code in Repo
1. package.json, package-lock.json, and requirements.txt are all in the root directory. Heroku will automatically look for these files there to install the dependencies.
2. Procfile runs the Django wsgi file with gunicorn
3. React app "src" and "public" folders are in the root directory (not inside another react app folder)
4. Static files directory is configured in "TEMPLATES" setting on settings.py
5. Django heroku called on last line of settings file configures databse, allowed hosts, etc. ([django_heroku documentation](https://pypi.org/project/django-heroku/))

# Change App Name
1. Change name of appname folder
2. Change any instance of "appname" to your project name in the following areas (use CTRL or CMD + F to find):
    1. appname/asgi.py (Line 14)
    2. appname/wsgi.py (Line 14)
    3. appname/settings.py (Line 54, Line 72)
