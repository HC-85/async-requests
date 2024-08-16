import aiohttp
import asyncio
from time import perf_counter

start_time = perf_counter()


async def get_pokemon(session, url):
    async with session.get(url) as response:
        pokemon = await response.json()
        return pokemon['name']


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, 152):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{i}'
            tasks.append(asyncio.ensure_future(get_pokemon(session, pokemon_url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)

asyncio.run(main())

print("--- %s seconds ---" % (perf_counter() - start_time))