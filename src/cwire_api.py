from requests import Session

from src.api.worker_api import WorkerApi


# Singleton
class CwireApi(object):
    _instance = None

    def __new__(cls, cwire, session: Session):
        if cls._instance is None:
            cls._instance = super(CwireApi, cls).__new__(cls)
            cls.cwire = cwire
            cls.api = session
            cls.api.headers.update({
                "X-API-KEY": cwire.api_key
            })
            cls.worker_api = WorkerApi(cwire=cwire, api=session)
            # cls.data_model_api = DataModelApi(cwire, session)
        return cls._instance

    async def create(cls):
        try:
            await cls.worker_api.create()
            # await self.data_model_api.create()
        except Exception as e:
            print("API initialising failed {message}".format(message=e))
