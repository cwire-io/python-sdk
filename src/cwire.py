from requests import Session

from src.cwire_api import CwireApi
from src.cwire_websocket import CwireWebSocket


# Singleton
class Cwire(object):
    _instance = None

    def __new__(cls, api_key: str, **kwargs):
        if cls._instance is None:
            cls._instance = super(Cwire, cls).__new__(cls)
            cls.api_key = api_key
            cls.api_url = 'https://api.cwire.io'
            cls.route = '/cwire'
            cls.models = kwargs.get('models')
            # cls.worker_functions = WorkerFunctions.create(cls)
            cls.websocket = CwireWebSocket(cwire=cls._instance)
            cls.api = CwireApi(cwire=cls._instance, session=Session())
            cls.worker = None
        return cls._instance

    def create(cls):
        if cls._instance:
            try:
                cls._instance.api.create()
                cls._instance.websocket.connect()
            except Exception as e:
                print("API initialising failed {message}".format(message=e))
                cls._instance.websocket.disconnect()
                del cls._instance
                cls._instance = None
            return cls._instance
