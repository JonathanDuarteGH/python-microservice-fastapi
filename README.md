# Python Microservice with FastAPI

This python project utilizes [FastAPI](https://fastapi.tiangolo.com/) to demonstrate how users would add movies and casts for purchase.

## Getting Started

1. Please install the following software before moving forward. **Restart is recommended** 

* [Python](https://www.python.org/downloads/)
* [PostgreSQL](https://www.postgresql.org/download/)
* [Docker](https://docs.docker.com/get-docker/)
* [FastAPI](https://fastapi.tiangolo.com/)

2. Copy the `docker-compose.yml` and place it within the root of your project folder.

```
version: '3.7'

services:
  movie_service:
    build: ./movie_service
    command: uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    volumes:
      - ./movie-service/:/app/
    ports:
      - 8001:8000
    environment:
      - DATABASE_URI=SERVER_NAME://USERNAME:PASSWORD@localhost/movie_db
      - CAST_SERVICE_HOST_URL=http://cast_service:8000/api/v1/casts/

  movie_db:
    image: postgres:12.1-alpine
    volumes:
      - postgres_data_movie:/var/lib/postgresql/data/
    environment:
      - POSTGRES_USER=USERNAME
      - POSTGRES_PASSWORD=PASSWORD
      - POSTGRES_DB=movie_db

  cast_service:
    build: ./cast_service
    command: uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    volumes:
      - ./cast-service/:/app/
    ports:
      - 8002:8000
    environment:
      - DATABASE_URI=SERVER_NAME://USERNAME:PASSWORD@localhost/casts_db

  cast_db:
    image: postgres:12.1-alpine
    volumes:
      - postgres_data_cast:/var/lib/postgresql/data/
    environment:
      - POSTGRES_USER=USERNAME
      - POSTGRES_PASSWORD=PASSWORD
      - POSTGRES_DB=casts_db

  nginx:
    image: nginx:latest
    ports:
      - "8080:8080"
    volumes:
      - ./nginx_config.conf:/etc/nginx/conf.d/default.conf
    depends_on:
      - cast_service
      - movie_service

volumes:
  postgres_data_movie:
  postgres_data_cast:
```

3. Replace the fields `SEVER_NAME`, `USERNAME`, and `PASSWORD` with your own credentials

4. Run the following `docker-compose up -d` in your terminal

5. There will be two browsers to launch in your docker desktop. Please open both of them and try to add, update, retrieve or delete a cast or a movie.

## Built With

* [Python](https://www.python.org/downloads/)
* [PostgreSQL](https://www.postgresql.org/download/)
* [Docker](https://docs.docker.com/get-docker/)
* [FastAPI](https://fastapi.tiangolo.com/)

## License

This project is subjected to the MIT License - see the [LICENSE.md](LICENSE.md) file for details