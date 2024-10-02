from app import create_app
from asgiref.wsgi import WsgiToAsgi

"""
Resources
    - Automatic routing with MethodViewResolver: https://connexion.readthedocs.io/en/latest/routing.html#automatic-routing-with-methodviewresolver
    - OpenAPI specification: https://swagger.io/specification/
"""

# production
app = create_app()
asgi_app = WsgiToAsgi(app)

# development
if __name__ == "__main__":
    app = create_app()
    app.run()
