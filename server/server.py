from aiohttp import web
from routes import setup_routes

def init_app():
    app = web.Application()
    setup_routes(app)
    return app

if __name__ == "__main__":
    app = init_app()
    web.run_app(app, port=8080)
