from typing import Sequence

from src.api.base_api import BaseApi
from src.cwire import DataModel


class DataModelApi(BaseApi):
    async def create(self):
        await self.clear_all_data_models()
        await self.sync_models(self.cwire.get_data_model_list())

    async def sync_models(self, models: Sequence[DataModel]):
        responses = []
        for model in models:
            responses.append(self.api.post('/models', model.to_json(())))
        return responses

    async def clear_all_data_models(self):
        return self.api.post("/models/clear")

    async def get_all_data_models(self):
        return self.api.get("/models")
