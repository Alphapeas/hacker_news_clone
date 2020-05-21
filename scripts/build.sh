#! /usr/bin/env sh

# Exit in case of error
set -e

docker-compose \
-f docker-compose.admin.yml \
-f docker-compose.base-images.yml \
-f docker-compose.build.yml \
-f docker-compose.command.yml \
-f docker-compose.depends.yml \
-f docker-compose.env.yml \
-f docker-compose.networks.yml \
-f docker-compose.ports.yml \
-f docker-compose.volumes.yml \
config > docker-stack.yml

docker-compose -f docker-stack.yml build
docker-compose -f docker-stack.yml up -d