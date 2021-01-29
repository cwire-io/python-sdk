from typing import Sequence

from src.data_model_field import DataModelField


class DataModelActionOptions:
    def __init__(self, name, action_type):
        self.name = name
        self.type = action_type


class DataModelOptions:
    def __init__(self, is_editable: bool = None, is_creatable: bool = None, is_deletable: bool = None, on_delete=None,
                 on_change=None, on_create=None, fields: Sequence[DataModelField] = None,
                 actions: Sequence[DataModelActionOptions] = None):
        self.is_editable = is_editable
        self.is_creatable = is_creatable
        self.is_deletable = is_deletable
        self.on_delete = on_delete
        self.on_change = on_change
        self.on_create = on_create
        self.fields = fields
        self.actions = actions


class DataModel:
    def __init__(self, name: str, options):
        self.name = name
        self.options = options
        self.type = options.get('type')

        if self.type == "Sqlalchemy":
            print("yeah")
            pass

    def init_sqlalchemy(self):
        pass


class DataModelFieldOptions:
    def __init__(self, field_type):
        self.type = field_type


class CwireOptions:
    def __init__(self, route: str = None, api_url: str = None, models: DataModel = None):
        self.route = route
        self.api_url = api_url
        self.models = models
