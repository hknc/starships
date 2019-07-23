# Starships

A Flask project that exposes a REST API endpoint

### Build & Start

Build and start the docker containers with docker-compose.

```sh
$ docker-compose -f dev.yml build
$ docker-compose -f dev.yml up
```

```sh
http://localhost:5000/api/list
```

### Serve with Nginx for production use

Edit [nginx settings](nginx/sites-enabled/flask_project)
Edit [.env file](.env)

```sh
$ docker-compose -f production.yml build
$ docker-compose -f production.yml up
```

```sh
http://localhost/api/list
```
