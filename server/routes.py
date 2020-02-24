from controllers.hello_world_controller import hello

def setup_routes(app):
    app.router.add_get('/', hello)
    app.router.add_get('/{name}', hello)

