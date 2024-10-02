import connexion
import pkg_resources
from connexion.resolver import MethodViewResolver, MethodResolver

API_SPEC = pkg_resources.resource_filename(__name__, "api/openapi.yaml")

# application factory function
def create_app(**kwargs):

    # define flask app
    app = connexion.FlaskApp(__name__)
    
    # register apis
    app.add_api(
        specification=API_SPEC, 
        resolver=MethodViewResolver(f'{__name__}.endpoints'),
        arguments={"custom_key": "custom_value"}
    )

    return app