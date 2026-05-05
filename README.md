# Buscador Técnico de Estadísticas - PokeAPI

## A. Definición del Contexto
**Stakeholder:** Analistas de datos de la Liga Pokémon y Entrenadores Profesionales.
**Propuesta de Valor:** Esta herramienta elimina la necesidad de consultar bases de datos externas lentas durante un torneo. Permite a los analistas obtener estadísticas base (Vida y Ataque) de forma instantánea mediante consola para decidir movimientos tácticos en tiempo real.

## B. Guía de Configuración
Para el correcto funcionamiento, se pueden configurar las siguientes variables de entorno:
* `POKEAPI_URL`: URL base para las consultas (por defecto: https://pokeapi.co/api/v2/pokemon/).

## C. Instrucciones de Ejecución (Docker)
1. Construir la imagen:
   ```bash
   docker build -t pokeapi-app .

   *[cite: 13-23]*

---

### 2. Crear el archivo `.gitignore`
Es un requisito obligatorio para evitar subir archivos basura o sensibles al repositorio[cite: 29, 57]. Crea un archivo llamado `.gitignore` (con el punto al principio) y pega esto:

docker run -it --name samplerunning pokeapi-app
