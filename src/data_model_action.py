from src.cwire import DataModelActionOptions


class DataModelAction:
    def __init__(self, name: str, options: DataModelActionOptions):
        self.name = name
        self.type = options.type

    def to_json(self):
        return {
            self.name,
            self.type
        }

    @staticmethod
    def is_valid_action_type(type):
        if not isinstance(type, str):
            return False

        # TODO Check if this works
        # return !!CWire.ACTIONS[type.toUpperCase()];
        return True
