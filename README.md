# gh-systems-challenge

This is a REST API with [Django](https://docs.djangoproject.com/en/4.2/), [Django REST Framework](https://www.django-rest-framework.org/) and [PostgreSQL](https://www.postgresql.org/docs/16/index.html).


## Overview: GH Systems API

Problem Statement proposed by [GH Systems]()


## Table of Contents

* [Overview](#gh-systems-challenge)
* [Main Dependencies](#Main-Dependencies)
* [Project Configuration](#Project-Configuration)


## Main Dependencies

    Python              ~3.12
    Django              ~4.2
    djangorestframework ~3.15
    PostgreSQL          ~16.6

For more details, see the [pyproject.toml file](pyproject.toml).

## Docker Configuration

- [Install Docker](https://docs.docker.com/engine/install/)

- [Install Docker Compose](https://docs.docker.com/compose/install/#install-compose)

## Project Configuration

- Clone this [repository](https://github.com/hugofer93/gh-systems-challenge):

        $ git clone https://github.com/hugofer93/gh-systems-challenge.git

- Create `.env` file based on `.env.sample`:

        $ cp .env.sample .env

    **Production or Staging Environment**:

    - Set `DEBUG=false`

    **Develop Environment**:

    - Set `DEBUG=true`

- Up Services with docker-compose:

        $ docker compose up -d

- Execute commands in container (e.g.):

        $ docker exec -it ghsystems_backend poetry run python manage.py createsuperuser

- Show container logs:

        $ docker compose logs -f backend
