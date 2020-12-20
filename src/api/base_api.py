class BaseApi:
    def __init__(self, cwire, api):
        self.cwire = cwire
        self.api = api

    @staticmethod
    def get_service_data(res):
        return res.data.data
