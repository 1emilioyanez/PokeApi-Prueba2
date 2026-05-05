#!/bin/bash

# Construir la imagen
echo "Construyendo la imagen pokeapi-app..."
docker build -t pokeapi-app .

# contenedor
echo "Iniciando el contenedor..."
docker run -it --name samplerunning pokeapi-app