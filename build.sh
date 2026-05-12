#!/bin/bash

# 1. Construir la imagen
echo "Construyendo la imagen pokeapi-app..."
docker build -t pokeapi-app .

# 2. Ejecutar el contenedor (sin -it para que no falle en Jenkins)
echo "Iniciando el contenedor..."
# Usamos el nombre 'samplerunning' como pide la guía para el Pipeline [cite: 67, 68]
docker run --name samplerunning pokeapi-app

# 3. Documentar la salida (Opcional pero recomendado para el output.txt) [cite: 33]
echo "Generando registro de salida..."
docker ps -a --filter "name=samplerunning" > output.txt
docker logs samplerunning >> output.txt
