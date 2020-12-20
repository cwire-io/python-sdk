from src.cwire import DataModelFieldOptions


class DataModelField:
    def __init__(self, name: str, options: DataModelFieldOptions):
        self.__name: str = name
        # TODO self.__is_primary: bool = options.
        self.__type: DataModelFieldOptions = options.type

    def to_json(self):
        return {
            "name": self.__name,
            "type": self.__type,
            "isPrimary": self.__is_primary
        }
