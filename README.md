
# App "News with Django3, DRF, docker-compose, Cron, PGAdmin, Postgresql"
* Here maybe I will deploy this app: http://boiling-oasis-95257.herokuapp.com/
* Git to heroku repo: https://github.com/Alphapeas/heroku_hn_clone.git
* Postman variables: https://www.getpostman.com/collections/1ebdf9fcc78aeb97838c
 ###All methods:
    # POST
    URI - post/list/ - GET, News posts list (all), pagination - ?page=x
    URI - post/create/ -  POST, News post creation (only authenticated)
    URI - post/update/<pk>/ -  PUT, PATCH, News post updating (only authenticated and owners or admins)
    URI - post/detail/<pk>/ -  GET, News post detail info (all users)
    URI - post/<int:pk>/vote/ -  POST, Add/delete vote (only authenticated)
    URI - post/delete/<pk>/ - DELETE, delete post (only admins)
    # COMMENT
    URI - comment/create/ - POST, create comment (only authenticated)
    URI - comment/list/?post=pk - GET, News post`s comments list (all users)
    URI - comment/update/<pk>/ - PUT, PATCH, update news post`s data (only authenticated and owners or admins)
    URI - comment/delete/<pk>/ - DELETE, delete comment (only admins)
## Backend Requirements

* Docker
* Docker Compose

## Backend local development

*First of all you need to specify vars in .env files

* Start the stack with Docker Compose:

```bash
docker-compose up -d
```
or
```bash
sh scripts/build.sh
```

* Now you can open your browser and interact with these URLs:

PGAdmin, PostgreSQL web administration: http://localhost:5050

Backend, JSON based web API based on OpenAPI: http://localhost:8000

**Note**: The first time you start your stack, it might take a minute for it to be ready. While the backend waits for the database to be ready and configures everything. You can check the logs to monitor it.

To check the logs, run:

```bash
docker-compose logs
```

To check the logs of a specific service, add the name of the service, e.g.:

```bash
docker-compose logs backend
```

## Backend local development, additional details

### General workflow

Open your editor at `./backend/app/` (instead of the project root: `./`), so that you see an `./app/` directory with your code inside. That way, your editor will be able to find all the imports, etc.

There is an `.env` file that has some Docker Compose default values that allow you to just run `docker-compose up -d` and start working, while still being able to use and share the same Docker Compose files for deployment, avoiding repetition of code and configuration as much as possible.

### Migrations

As during local development your app directory is mounted as a volume inside the container (set in the file `docker-compose.dev.volumes.yml`), you can also run the migrations with `alembic` commands inside the container and the migration code will be in your app directory (instead of being only inside the container). So you can add it to your git repository.

* Start an interactive session in the backend container:

```bash
docker-compose exec backend bash
```

* If you created a new model for Django application

```bash
python manage.py makemigrations yourappname
```

* After creating migration

```bash
python manage.py migrate
```
* After migrating you can enter to you development server
```