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
    global names
    start = time.time()
    response = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=150')
    data = response.json()
    files = open('pokemons.txt', 'a')
    pokemons = data['results'] 
    for pokemon in pokemons:
        names.append(pokemon['name'])
    names = ' '.join(names)
    files.write(names)
    files.close()
    end = time.time()
    print(f"Время выполнения: {end-start:.3f} s")

asyncio.run(response_get())
