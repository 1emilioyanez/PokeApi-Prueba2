import requests

# Funcion principal para buscar datos del pokemon
def buscar_pokemon():
    print("\n--- POKE-BUSCADOR INTERACTIVO ---")
    # Captura el nombre y limpia espacios o mayusculas
    nombre = input("Escribe el nombre de un Pokémon (o 'salir'): ").lower().strip()
    
    # Condicion de salida del bucle
    if nombre == 'salir':
        return False

    # URL base de la PokeAPI
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"

    try:
        # Realiza la peticion GET con un tiempo limite de 10 segundos
        response = requests.get(url, timeout=10)
        # Verifica si el codigo de estado HTTP es exitoso
        response.raise_for_status() 
        # Convierte la respuesta a formato diccionario de Python
        data = response.json()
        
        # Extrae datos especificos del JSON segun su estructura
        vida = data['stats'][0]['base_stat']
        ataque = data['stats'][1]['base_stat']
        foto = data['sprites']['front_default']

        # Muestra los resultados en pantalla
        print(f"\n¡ENCONTRADO!")
        print(f"Nombre: {data['name'].capitalize()}")
        print(f"HP (Vida): {vida}")
        print(f"Ataque: {ataque}")
        print(f"URL Imagen: {foto}")

    # Gestion de errores especificos de la libreria requests y formato
    except requests.exceptions.HTTPError:
        print(f"Error 1 (HTTP): No se encontro a '{nombre}'.")
        
    except requests.exceptions.ConnectionError:
        print("Error 2 (Conexion): Problema de red o internet.")
        
    except requests.exceptions.Timeout:
        print("Error 3 (Timeout): Tiempo de respuesta excedido.")

    except ValueError:
        print("Error 4 (Formato): Respuesta no es un JSON valido.")

    return True

# Bloque de ejecucion continua
corriendo = True
while corriendo:
    corriendo = buscar_pokemon()