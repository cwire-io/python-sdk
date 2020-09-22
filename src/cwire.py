from typing import Sequence


class data_model_action_options:
    def __init__(self, action_type):
        self.type = action_type


class data_model_action:
    def __init__(self, name: str, options: data_model_action_options):
        self.name = name
        self.type = options.type


class data_model_field_options:
    def __init__(self, field_type):
        self.type = field_type


class data_model_field:
    def __init__(self, name: str, options: data_model_field_options):
        self.name = name
        self.type = options.type


class data_model_options:
    def __init__(self, is_editable: bool = None, is_creatable: bool = None, is_deletable: bool = None, on_delete=None,
                 on_change=None, on_create=None, fields: Sequence[data_model_field] = None,
                 actions: Sequence[data_model_action_options] = None):
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
class data_model:
    def __init__(self, name: str, identifier: str, options: data_model_options):
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


class cwire_options:
    def __init__(self, route: str, api_url: str, models: Sequence[data_model]):
        self.route = route
        self.api_url = api_url
        self.models = models


class cwire:
    def __init__(self, api_key: str, options: cwire_options):
        self.api_key = api_key

        if options.api_url:
            self.cwire_api_url = options.api_url
