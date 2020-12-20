from src.api.base_api import BaseApi
from src.helper.api import parse_response


class WorkerApi(BaseApi):
    @classmethod
    async def create(self):
        self.cwire.set_worker(await self.get_worker_info())

    async def get_worker_info(self):
        try:
            return parse_response(await self.api.get("/auth/api-clients/me"))
        except Exception as e:
            print("Worker not found {message}".format(message=e))
