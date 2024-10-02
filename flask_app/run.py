from flask import send_from_directory
from app import create_app
from os.path import dirname, join
from pathlib import Path

# from . import auth

"""
Resources
    - Automatic routing with MethodViewResolver: https://connexion.readthedocs.io/en/latest/routing.html#automatic-routing-with-methodviewresolver
    - OpenAPI specification: https://swagger.io/specification/
"""

app = create_app()

if __name__ == "__main__":

    # start the server with auto reloading
    app.run(f'{Path(__file__).stem}:app')
