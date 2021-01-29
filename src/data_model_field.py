class DataModelField:
    def __init__(self, name: str, options):
        self.__name: str = name
        self.__is_primary: bool = options.is_primary
        self.__type = options.type

    def to_json(self):
        return {
            "name": self.__name,
            "type": self.__type,
            "isPrimary": self.__is_primary
        }
