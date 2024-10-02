import pkg_resources
import random
import connexion

from connexion.resolver import MethodViewResolver
from flask import send_from_directory
from os.path import dirname, join
from . import auth

"""
Resources
    - Automatic routing with MethodViewResolver: https://connexion.readthedocs.io/en/latest/routing.html#automatic-routing-with-methodviewresolver
    - OpenAPI specification: https://swagger.io/specification/
"""

API_SPEC = pkg_resources.resource_filename(__name__, "openapi/swagger.yaml")
# OPTIONS = {"swagger_url": "/docs"}

# application factory function
def create_app(**kwargs):
    print(f'- defining ASGI application instance called {__name__}')
    app = connexion.FlaskApp(__name__)
    app.add_api(API_SPEC, resolver=MethodViewResolver(__name__.split(".")[0]))

    return app