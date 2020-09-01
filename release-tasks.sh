#Delete these after first deploy
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations api

#Keep these (and add them for every app that you want to migrate)
python manage.py migrate api