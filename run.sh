#!/bin/bash

# Build the Docker image
docker build -t docker-project .

# Create the dataset and output directories if they don't exist
mkdir -p dataset
mkdir -p output

# Run the Docker container with mounted volumes
docker run --rm -v $(pwd)/dataset:/usr/local/dataset -v $(pwd)/output:/usr/local/output docker-project