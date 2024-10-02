from flask import make_response, request
from flask.views import MethodView

class FlasktemplateView(MethodView):
    
    """
    Views for endpoints which return xxxxx
    """

    def post(self, body:dict):
        return make_response(f'{body}', 200)

    def put(self):
        pass

    def delete(self):
        pass

    def get(self, **kwargs):
        return make_response(f'get: url configured correctly kwargs: {kwargs}', 200)

    # def search(self, **kwargs):
    #     print(f"Received kwargs: {kwargs}")  # Log all keyword arguments
    #     print(f"Request args: {request.args}")  # Log query parameters
    #     return make_response(f'get: url configured correctly kwargs: {kwargs}', 200)