from typing import Sequence

import socketio

from src.cwire_api import CwireApi
from src.cwire_websocket import CwireWebSocket
from src.data_model_field import DataModelField
from src.worker.functions import WorkerFunctions


class DataModelActionOptions:
    def __init__(self, name, action_type):
        self.name = name
        self.type = action_type


class DataModelFieldOptions:
    def __init__(self, field_type):
        self.type = field_type


class DataModelOptions:
    def __init__(self, is_editable: bool = None, is_creatable: bool = None, is_deletable: bool = None, on_delete=None,
                 on_change=None, on_create=None, fields: Sequence[DataModelField] = None,
                 actions: Sequence[DataModelActionOptions] = None):
        self.is_editable = is_editable
        self.is_creatable = is_creatable
        self.is_deletable = is_deletable
        self.on_delete = on_delete
        self.on_change = on_change
        self.on_create = on_create
        self.fields = fields
        self.actions = actions


class CwireOptions:
    def __init__(self, route: str = None, api_url: str = None, models: DataModel = None):
        self.route = route
        self.api_url = api_url
        self.models = models


class Cwire:
    api_url: str
    CWIRE_ROUTE = '/cwire'
    CWIRE_API_URL = 'https://api.cwire.io'

    def __init__(self, api_key: str, **kwargs):
        self.api_key = api_key
        self.api_url = kwargs.get('api_url')
        self.route = kwargs.get('route')
        self.models = kwargs.get('models')
        self.worker = WorkerFunctions.create(self)
        self.websocket = CwireWebSocket(self)
        self.api = CwireApi(self, socketio.AsyncClient())
        self.instance = None

    async def create(self, api_key, options):
        if self.instance is None:
            try:
                self.instance = Cwire(api_key, options)
                await self.instance.api.create()
                await self.instance.websocket.connect()
            except Exception as e:
                print("API initialising failed {message}".format(message=e))
                self.instance.websocket.disconnect()
                del self.instance
                self.instance = None

        return self.instance
