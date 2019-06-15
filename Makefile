APP_NAME=app-dev


start_docker:
	docker-compose up -d

stop_docker:
	docker-compose stop

app_restart:
	docker-compose restart $(APP_NAME)

app_logs:
	docker-compose logs -f $(APP_NAME)

app_attach:
	docker-compose exec $(APP_NAME) /bin/zsh

all_logs:
	docker-compose logs -f

down_docker:
	docker-compose down

rebuild_docker:
	docker-compose up --force-recreate --build -d

force_rebuild_docker: down_docker rebuild_docker

build:
	docker login
	docker-compose -f docker-compose-build.yml build

push:
	docker login
	docker-compose -f docker-compose-build.yml push

build_push: build push
