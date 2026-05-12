@echo off

echo =========================
echo DETENIENDO CONTENEDOR
echo =========================

docker stop samplerunning
docker rm samplerunning

echo =========================
echo CONSTRUYENDO IMAGEN
echo =========================

docker build -t sampleapp .

echo =========================
echo EJECUTANDO CONTENEDOR
echo =========================

docker run --name samplerunning sampleapp

echo =========================
echo FINALIZADO
echo =========================
