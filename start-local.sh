#!/usr/bin/env bash

###start a local mysql server
MYSQL_CONTAINER_NAME=bicycle-db
if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    docker rm -f MYSQL_CONTAINER_NAME
fi

docker run -d --restart always --name $MYSQL_CONTAINER_NAME -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=bicycle-db -v ~/data/bicycle-db:/var/lib/mysql mysql:5.6.40 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci

###start a redis server
REDIS_CONTAINER_NAME=bicycle-redis
if [ "$(docker ps -q -f name=REDIS_CONTAINER_NAME)" ]; then
    docker rm -f REDIS_CONTAINER_NAME
fi
docker run -d --restart always -p 6379:6379 --name REDIS_CONTAINER_NAME -v ~/data/bicycle-redis:/data redis

##
python3 ./manage.py makemigrations users

python3 ./manage.py migrate users

python3 manage.py runserver