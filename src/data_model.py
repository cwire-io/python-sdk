from src.cwire import DataModelOptions
from src.data_model_action import DataModelAction
from src.data_model_field import DataModelField


class DataModel:
    def __init__(self, name: str, identifier: str = None, data_model_options: DataModelOptions = None,
                 fields: DataModelField = None, actions: DataModelAction = None):
        self.name = name
        self.id = identifier
        self.data_model_options = data_model_options
        self.fields = fields
        self.actions = actions