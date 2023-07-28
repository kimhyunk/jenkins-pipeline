#!/usr/bin/env bash

set -Eeuo pipefail
trap cleanup SIGINT SIGTERM ERR EXIT
cleanup() {
    trap - SIGINT SIGTERM ERR EXIT
    exit
}
DOCKER_REG="docker.falinux.dev"
DOCKER_PATH="services"
DOCKER_REG_USER="falinux"
DOCKER_REG_PASSWORD="2001May09"
DOCKER_IMG_NAME="falinux-supercom-backend"
DOCKER_IMG_TAG="latest"

echo ""
echo "Docker image build and push registry ..."
echo ""

# docker-compose build --no-cache falinux-services-supercom-backend
docker-compose build falinux-services-supercom-backend

docker tag ${DOCKER_PATH}/${DOCKER_IMG_NAME}:${DOCKER_IMG_TAG} ${DOCKER_REG}/${DOCKER_PATH}/${DOCKER_IMG_NAME}:${DOCKER_IMG_TAG}
docker login -u ${DOCKER_REG_USER} -p ${DOCKER_REG_PASSWORD} ${DOCKER_REG}
docker tag ${DOCKER_PATH}/${DOCKER_IMG_NAME} ${DOCKER_REG}/${DOCKER_PATH}/${DOCKER_IMG_NAME}:${DOCKER_IMG_TAG}
docker push ${DOCKER_REG}/${DOCKER_PATH}/${DOCKER_IMG_NAME}:${DOCKER_IMG_TAG}
docker logout ${DOCKER_REG}

kubectl --kubeconfig ~/.kube/config-clone -n supercom rollout restart deployment/backend
