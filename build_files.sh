pip install -r requirements.txt 
python3.11 manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py test