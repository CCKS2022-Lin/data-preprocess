#!/usr/bin/env bash

docker pull mongo
docker run --name mongo -p 27017:27017 -d mongo
