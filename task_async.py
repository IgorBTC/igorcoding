import asyncio
import requests
import json
import pprint
import time

data = []
pokemons = []
names = []
start: float
end: float

async def response_get():
    start = time.time()
    response = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=150')
    data = response.json()
    pokemons = data['results']  # твой список словарей
    for pokemon in pokemons:
        names.append(pokemon['name'])
    pprint.pprint(names)
    end = time.time()
    print(f"Время выполнения: {end-start:.3f} s")

asyncio.run(response_get())
