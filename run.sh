python manage.py migrate
python manage.py collectstatic --no-input
uwsgi --http :8008 --module website.wsgi:application