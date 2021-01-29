from src.api.base_api import BaseApi
from src.helper.api import parse_response


# Singleton
class WorkerApi(BaseApi):
    _instance = None

    def __new__(cls, **kwargs):
        if cls._instance is None:
            cls._instance = super(WorkerApi, cls).__new__(cls)
        return cls._instance

    def create(cls):
        cls._instance.cwire.worker(cls.get_worker_info())

    @classmethod
    def get_worker_info(cls):
        try:
            # TODO get api url from cwire instance
            return parse_response(cls._instance.api.get("https://api.cwire.io" + "/auth/api-clients/me"))
        except Exception as e:
            print("Worker not found {message}".format(message=e))
