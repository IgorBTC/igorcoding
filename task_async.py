import asyncio
import requests
import json
import pprint
import time

data, data_1 = [], []
pokemons, pokemons_1 = [], []
names, names_1 = [], []
start: float
start_1: float
end: float
end_1: float

async def response_get():
    global names
    start = time.time()
    response = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=150')
    data = response.json()
    files = open('pokemons_async.txt', 'a')
    pokemons = data['results'] 
    for pokemon in pokemons:
        names.append(pokemon['name'])
    names = ' '.join(names)
    files.write(names)
    files.close()
    end = time.time()
    print(f"Время выполнения: {end-start:.3f} s")

def responce_common(data_1, names_1):
    start_1 = time.time()
    for id in range(1, 151):
        response_1 = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}/')
        data_1 = response_1.json()
        names_1.append(data_1['name'])
    names_1 = ' '.join(names_1)
    files_1 = open('pokemons.txt', 'a')
    files_1.write(names_1)
    files_1.close()
    end_1 = time.time()
    print(f"Время выполнения синхронной функции: {end_1-start_1:.3f} s")

asyncio.run(response_get())
responce_common(data_1, names_1)