create-venv:
	python3 -m venv venv

activate-venv:
	source venv/bin/activate

install-requirements:
	sudo apt-get install tesseract-ocr
	venv/bin/pip install -r requirements.txt

run:
	venv/bin/python manage.py runserver 0.0.0.0:8000

recreate_db:
	venv/bin/python manage.py recreate_db

migration:
	venv/bin/python manage.py makemigrations; venv/bin/python manage.py migrate

clean_pdf:
	rm -Rf media/*
	rm db.*
	venv/bin/python manage.py migrate
	venv/bin/python manage.py createsuperuser