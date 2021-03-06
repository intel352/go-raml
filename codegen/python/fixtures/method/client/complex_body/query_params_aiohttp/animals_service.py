# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.
from .animal import animal
from .unhandled_api_error import UnhandledAPIError
from .unmarshall_error import UnmarshallError


class AnimalsService:
    def __init__(self, client):
        self.client = client

    async def animals_get(self, name, nodef, depth=1, inspect=false, headers=None, query_params=None, content_type="application/json"):
        """
        test query params
        It is method for GET /animals
        """
        if query_params is None:
            query_params = {}

        query_params['depth'] = depth
        query_params['inspect'] = inspect
        query_params['name'] = name
        query_params['nodef'] = nodef

        uri = self.client.base_url + "/animals"
        resp = await self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status == 201:
                resps = []
                for elem in resp.json():
                    resps.append(animal(elem))
                return resps, resp
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except Exception as e:
            raise UnmarshallError(resp, e.message)
