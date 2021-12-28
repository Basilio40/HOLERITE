create-venv:
	python3 -m venv venv

activate-venv:
	source venv/bin/activate

install-requirements:
	venv/bin/pip install -r requirements.txt

run:
	python3 manage.py runserver 0.0.0.0:5000

recreate_db:
	python3 manage.py recreate_db

migration:
	python3 manage.py makemigrations; python3 manage.py migrate