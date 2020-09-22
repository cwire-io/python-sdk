from typing import Sequence


class DataModelActionOptions:
    def __init__(self, name, action_type):
        self.name = name
        self.type = action_type


class DataModelAction:
    def __init__(self, name: str, options: DataModelActionOptions):
        self.name = name
        self.type = options.type


class DataModelFieldOptions:
    def __init__(self, field_type):
        self.type = field_type


class DataModelField:
    def __init__(self, name: str, options: DataModelFieldOptions):
        self.name = name
        self.type = options.type


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


# fields: Mapping[str, data_model_field],
# actions: Mapping[str, data_model_action]
class DataModel:
    def __init__(self, name: str, identifier: str, options: DataModelOptions):
        self.name = name
        self.id = identifier
        self.options = options
        self.fields = []
        self.actions = []

        if options.fields:
            for field in options.fields:
                self.fields.append([field.name, field.type])
        if options.actions:
            for action in options.actions:
                self.actions.append([action.name, action.type])


class CwireOptions:
    def __init__(self, route: str, api_url: str, models: Sequence[DataModel]):
        self.route = route
        self.api_url = api_url
        self.models = models


class Cwire:
    def __init__(self, api_key: str, options: CwireOptions):
        self.api_key = api_key

        if options.api_url:
            self.cwire_api_url = options.api_url
