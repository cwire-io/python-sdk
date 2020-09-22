from typing import Sequence

from src.cwire import DataModel


class BaseApi:
    def __init__(self, cwire, api):
        self.cwire = cwire
        self.api = api

    @staticmethod
    def get_service_data(res):
        # TODO
        return res.data.data


class DataModelApi(BaseApi):
    async def create(self):
        await self.clear_all_data_models()
        await self.sync_models()

    async def clear_all_data_models(self):
        return self.api.post("/models/clear")

    async def sync_models(self, models: Sequence[DataModel]):
        # TODO
        pass

    async def get_all_data_models(self):
        return self.api.get("/models")


class TunnelApi(BaseApi):
    async def create_tunnel(self):
        return await BaseApi.get_service_data(self.api.post("/tunnels"))


class CwireApi:
    def __init__(self, api, cwire, tunnel_api, data_model_api):
        self.api = api
        self.cwire = cwire
        self.tunnel_api = tunnel_api
        self.data_model_api = data_model_api
