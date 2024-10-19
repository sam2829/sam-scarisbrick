release: python manage.py makemigrations && python manage.py migrate
web: gunicorn my_portfolio.my_portfolio.wsgi --log-file -