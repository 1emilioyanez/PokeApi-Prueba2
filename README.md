# 🚀 Proyecto PokeAPI - Automatización y Contenerización

## 📝 Introducción
Este proyecto es una aplicación interactiva desarrollada en **Python** que consume datos de la **PokeAPI**. El objetivo principal es demostrar habilidades en el ciclo de vida de desarrollo de software (SDLC) mediante la **contenerización** con Docker y la **automatización de despliegue** (CI/CD) utilizando Jenkins.

La aplicación permite al usuario consultar información básica de cualquier Pokémon (Nombre, HP, Ataque) y manejar errores de conexión o datos no encontrados de manera segura.

---

## 🌟 Propuesta de Valor
Este sistema resuelve el problema de la consistencia en los entornos de ejecución. Al utilizar **Docker**, garantizamos que la aplicación funcione exactamente igual en la máquina de un desarrollador, en el servidor de la universidad o en la nube, eliminando el clásico "en mi máquina sí funciona".

---

## 🏗️ Requisitos del Sistema
Para ejecutar este proyecto, necesitas tener instalados:
* **Docker**: Para construir y correr el contenedor.
* **Jenkins**: Para la orquestación del Pipeline de automatización.
* **Git**: Para el control de versiones.
* **Python 3.10+**: (Opcional, si se corre fuera de Docker).

---

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python (librería `requests`).
* **Contenerización:** Docker (Imagen base `python:3.10-slim`).
* **CI/CD:** Jenkins (Pipeline as Code).
* **Seguridad:** Uso de la librería `os` para manejo de variables de entorno y protección de rutas.

---

## 🚀 Instrucciones de Ejecución

### 1. Clonar el repositorio
```bash
git clone [https://github.com/1emilioyanez/PokeApi-Prueba2.git](https://github.com/1emilioyanez/PokeApi-Prueba2.git)
cd PokeApi-Prueba2
