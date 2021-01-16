from requests import Session


class BaseApi:
    def __init__(self, cwire, api: Session):
        self.api = api
        self.cwire = cwire

    @staticmethod
    def get_service_data(res):
        return res.data.data
