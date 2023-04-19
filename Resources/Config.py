import yaml


class Config:
    _instance = None
    _config = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            with open('Resources/config.yml') as stream:
                cls._config = yaml.safe_load(stream)['database']
        return cls._instance

    @staticmethod
    def get(key):
        return Config()._config.get(key)
