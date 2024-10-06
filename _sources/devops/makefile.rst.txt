***************
Docker Makefile
***************

.. code-block:: console

    include .env_vars/.env
    include .env_vars/.env.wse

    ifeq (${ENVIRONMENT}, development)
        COMPOSE := docker compose -f docker-compose.dev.yml
    else ifeq (${ENVIRONMENT}, production)
        COMPOSE := docker compose -f docker-compose.prod.yml
    endif

    APP := @$(COMPOSE) exec wse-project
    MANAGE := @$(APP) python manage.py


    # Docker
    update:
        @$(COMPOSE) down wse-project && \
        $(COMPOSE) up wse-project -d


    build:
        @$(COMPOSE) build

    up:
        @$(COMPOSE) up -d

    down:
        @$(COMPOSE) down

    restart: ruff down build up

    docker-clean:
        @$(COMPOSE) down && \
        docker image prune -a -f && \
        docker volume prune -a -f && \
        docker builder prune -a -f && \
        docker system df
