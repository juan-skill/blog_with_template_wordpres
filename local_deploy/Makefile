# Project Targets

.PHONY: create-project build-docker run status clean

build:
	make build-docker
	make migrate-python

create-django-project:
	docker-compose run backend django-admin startproject $(PROJECT_NAME) .

create-django-app:
	docker-compose exec backend django-admin startapp $(APP_NAME)

manage-python:
	docker-compose exec backend python manage.py $(command)

create-vue-project:
	docker-compose run frontend vue create .

build-docker:
	docker-compose build

run:
	docker-compose up -d $(service)

# docker-compose logs -f
logs:
	docker-compose logs $(service)

status:
	docker-compose ps -a

down:
	docker-compose down

db1clean:
	[ -d ../data/ ] && sudo rm -rf ../data/

m1clean:
	[ -d ../backend/applications/base/migrations/ ] && sudo rm -rf ../backend/applications/base/migrations/0*

# for f in ./*/*/migrations/*0*; do [ -f $f ] && sudo rm $f done
# sudo rm ./*/*/migrations/*0*

# -------------------------------------------------------------------------------------------
upbankend1: service=backend
upbankend1: run
upb1: upbankend1

logsbankend1: service=backend
logsbankend1: logs
logb1: logsbankend1

logsdatabase1: service=db
logsdatabase1: logs
logdb1: logsdatabase1


upvue: service=vuefrontend
upvue: run
upfd: upvue

logsvue: service=vuefrontend
logsvue: logs
logfd: logsvue

makemigrations-python: command=makemigrations
makemigrations-python: manage-python
mm: makemigrations-python

migrate-python: command=migrate
migrate-python: manage-python

manage-createsuperuser: command=shell -c "from blog.models import User; User.objects.create_superuser(username='root', email='admin@example.com', name='hack', last_name='er', password='passenger') if User.objects.filter(email='admin@example.com').first() is None else None;"
manage-createsuperuser: manage-python
csu: manage-createsuperuse

lint:
	docker-compose run --rm web flake8

bash:
	docker-compose run --rm web sh
