from src.cwire import Cwire


class WorkerFunctions:
    def __init__(self, cwire: Cwire):
        self.instance = None
        self.cwire = cwire
        # self.functions = dict[str, IWorkerFunction]

    def add_function(self):
        fn_instance = self.cwire
        # TODO

    def create(self, cwire: Cwire):
        if not self.instance:
            self.instance = WorkerFunctions(cwire)

        return self.instance
