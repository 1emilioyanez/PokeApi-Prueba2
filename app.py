import requests
import os

# Funcion principal para buscar datos del pokemon
def buscar_pokemon():
    api_url_base = os.getenv('POKEAPI_URL', 'https://pokeapi.co/api/v2/pokemon/')
    
    print("\n--- POKE-BUSCADOR INTERACTIVO ---")
    nombre = input("Escribe el nombre de un Pokémon (o 'salir'): ").lower().strip()
    
    if nombre == 'salir':
        return False

    url = f"{api_url_base}{nombre}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() 
        data = response.json()
        
        vida = data['stats'][0]['base_stat']
        ataque = data['stats'][1]['base_stat']
        foto = data['sprites']['front_default']

        print(f"\n¡ENCONTRADO!")
        print(f"Nombre: {data['name'].capitalize()}")
        print(f"HP (Vida): {vida}")
        print(f"Ataque: {ataque}")
        print(f"URL Imagen: {foto}")

    # Manejo de 4 errores 
    except requests.exceptions.HTTPError:
        print(f"Error 1 (HTTP): No se encontro a '{nombre}'.")
    except requests.exceptions.ConnectionError:
        print("Error 2 (Conexion): Problema de red o internet.")
    except requests.exceptions.Timeout:
        print("Error 3 (Timeout): Tiempo de respuesta excedido.")
    except ValueError:
        print("Error 4 (Formato): Respuesta no es un JSON valido.")

    return True

if __name__ == "__main__":
    corriendo = True
    while corriendo:
        corriendo = buscar_pokemon()
