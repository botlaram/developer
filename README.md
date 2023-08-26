# learning_python
the Repo contents all python learning task along with mkdocs

## create python env
> python -m venv venv

## activate env
> venv\Scripts\activate

## install required packages
> pip install -r requirements.txt

## to host documentation
> mkdocs serve

# host mkdocs using dockerfile

### run docker file

> docker build -t mkdocs-docker .

> docker run -p 8000:8000 mkdocs-docker

### to debug in container

> docker run -p 8000:8000 mkdocs-docker

## run docker-composer yaml file

> docker-compose up -d

> docker exec -it <container-name> "bash"

# host Mkdocs using Git repo

### run docker file
> docker build -t mkdocs-docker .

### start container
> docker run -p 8000:8000 mkdocs-docker

### hit the below url for mkdocs
http://localhost:8000/
