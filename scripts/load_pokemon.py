import sys

import requests


def fetch_pokemon_moves_and_create(auth_token, offset):
    """
    Fetch all Pokémon types from the PokeAPI and send them to the Django backend.
    """
    pokeapi_url = f"https://pokeapi.co/api/v2/pokemon/?limit=100000&offset={offset}"
    django_backend_url = "http://localhost:8000/api/pokemon/"

    headers = {
        "Authorization": f"Token {auth_token}"
    }

    try:
        # Fetch Pokémon types from the PokeAPI
        response = requests.get(pokeapi_url)
        response.raise_for_status()
        data = response.json()
        type_keys = []
        ability_keys = []
        move_keys = []

        # Iterate through the results and send POST requests to the Django backend
        for info in data.get("results", []):
            # Fetch type details to get the ID
            details = requests.get(info["url"]).json()
            id = details["id"]
            name = info["name"]
            height = details["height"]
            weight = details["weight"]
            base_experience = details["base_experience"]
            order = details["order"]
            is_default = details["is_default"]

            # Get types
            for type in details["types"]:
                key = type["type"]["url"].split("/")[-2]
                type_keys.append(int(key))

            # Get abilities
            for ability in details["abilities"]:
                key = ability["ability"]["url"].split("/")[-2]
                ability_keys.append(int(key))

            # Get moves
            for move in details["moves"]:
                key = move["move"]["url"].split("/")[-2]
                move_keys.append(int(key))

            # Prepare the payload for the POST request
            payload = {
                "id": id,
                "name": name,
                "height": height,
                "weight": weight,
                "base_experience": base_experience,
                "order": order,
                "is_default": is_default,
                "type_keys": type_keys,
                "ability_keys": ability_keys,
                "move_keys": move_keys
            }

            # Send the POST request to the Django backend
            post_response = requests.post(
                django_backend_url, json=payload, headers=headers)

            if post_response.status_code == 201:
                print(
                    f"Successfully created type: ID={id}, Name={name}")
            else:
                print(
                    f"Failed to create type: ID={id}, Name={name}, Error={post_response.text}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fetch_pokemon_types_and_create.py <auth_token>")
        sys.exit(1)

    auth_token = sys.argv[1]
    offset = sys.argv[2] if len(sys.argv) == 3 else 0
    fetch_pokemon_moves_and_create(auth_token, offset)
