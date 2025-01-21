import sys

from .load_abilities import fetch_pokemon_abilities_and_create
from .load_moves import fetch_pokemon_moves_and_create
from .load_pokemon import fetch_pokemon_and_create
from .load_types import fetch_pokemon_types_and_create


def load_all(token):
    fetch_pokemon_types_and_create(token, 0)
    fetch_pokemon_abilities_and_create(token, 0)
    fetch_pokemon_moves_and_create(token, 0)
    fetch_pokemon_and_create(token, 0)


if __name__ == '__main__':
    if sys.argc != 2:
        print("Usage: python load_all_pokemon_data.py <auth_token>")
        sys.exit(1)

    auth_token = sys.argv[1]
    load_all(auth_token)
