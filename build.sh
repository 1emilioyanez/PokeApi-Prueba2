#!/bin/bash

# 1. Construir la imagen
echo "Construyendo la imagen pokeapi-app..."
docker build -t pokeapi-app .

# 2. Ejecutar el contenedor
echo "Iniciando el contenedor..."
docker run --name samplerunning pokeapi-app

# 3. Documentar la salida
echo "Generando registro de salida..."
docker ps -a --filter "name=samplerunning" > output.txt
docker logs samplerunning >> output.txt
