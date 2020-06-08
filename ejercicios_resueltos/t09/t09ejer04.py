import asyncio
import aiohttp
import json

# Completa este metodo
@asyncio.coroutine
def fetch_page(url):
    """
        Imprime por pantalla la url y el contenido de la misma, cargando la url
        mediante aiohttp
    """
    response = yield from aiohttp.request('GET', url)
    assert response.status == 200
    content = yield from response.read()
    print('URL: {0}:  Content: {1}'.format(url, json.loads(content.decode('utf-8'))))


loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(fetch_page('http://jsonplaceholder.typicode.com/posts/1')),
    asyncio.ensure_future(fetch_page('http://jsonplaceholder.typicode.com/posts/2')),
    asyncio.ensure_future(fetch_page('http://jsonplaceholder.typicode.com/posts/3'))]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
