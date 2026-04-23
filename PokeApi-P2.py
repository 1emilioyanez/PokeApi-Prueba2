import requests

def buscar_pokemon():
    print("\n--- POKE-BUSCADOR INTERACTIVO ---")
    nombre = input("Escribe el nombre de un Pokémon (o 'salir'): ").lower().strip()
    
    if nombre == 'salir':
        return False

    url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"

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

    except requests.exceptions.HTTPError:
        print(f"Error 1 (HTTP): No se encontró a '{nombre}'. Revisa la ortografía.")
        
    except requests.exceptions.ConnectionError:
        print("Error 2 (Conexión): Fallo de red. Revisa tu internet.")
        
    except requests.exceptions.Timeout:
        print("Error 3 (Timeout): El servidor tardó demasiado en responder.")

    except ValueError:
        print("Error 4 (Formato): La respuesta de la API no es un JSON válido.")

    return True

corriendo = True
while corriendo:
    corriendo = buscar_pokemon()