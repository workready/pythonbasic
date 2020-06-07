import asyncio
import aiohttp
import json

async def get_json(client, url):
    """Llama a la url y envia su contenido a la corrutina llamante"""
    async with client.get(url) as response:
        pass    # Tu codigo aqui

async def get_reddit_top(subreddit, client):
    """Llama a la corrutina get_json para obtener, en formato JSON, el contenido que nos interesa"""
    pass    # Tu codigo aqui

# Podemos definir una función main y llamarla como vemos abajo.
def main():
    loop = asyncio.get_event_loop()

    # Crea un cliente HTTP con aiohttpClientSession
    # Doc: http://aiohttp.readthedocs.io/en/stable/client_reference.html#client-session
    client = aiohttp.ClientSession(loop=loop)

    # Añade tres llamadas a get_reddit_top como subtareas. 
    tasks = [
        asyncio.ensure_future(get_reddit_top('python', client)),
        asyncio.ensure_future(get_reddit_top('programming', client)),
        asyncio.ensure_future(get_reddit_top('compsci', client))
    ]

    # Ejecuta las tareas
    loop.run_until_complete(asyncio.wait(tasks))

    # Termina el bucle y cierra el cliente http
    loop.stop()
    client.close()


if __name__ == "__main__":  # <1>
    main()