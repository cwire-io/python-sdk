from src.api.datamodel_api import DataModelApi
from src.api.worker_api import WorkerApi


class CwireApi:
    def __init__(self, cwire, socket):
        self.api = socket
        self.cwire = cwire
        self.worker_api = WorkerApi(cwire, socket)
        self.data_model_api = DataModelApi(cwire, socket)

    async def create(self):
        try:
            await self.worker_api.create()
            await self.data_model_api.create()
        except Exception as e:
            print("API initialising failed {message}".format(message=e))

    def get_socket(self):
        return self.api
