from aiohttp import web

async def hello(request):
    name = request.match_info.get('name', 'World')
    text = f"Hello, {name}!"
    print('recived request, replying with "{}".'.format(text))
    return web.Response(text=text)