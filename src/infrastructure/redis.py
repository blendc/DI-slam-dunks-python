from infrastructure.config import AppEnv


class RedisConfig:
    def __init__(self, host, port, app_env: AppEnv, password=None):
        self.host = host
        self.port = port
        self.app_env = app_env
        self.password = password
        self.db_number_env = {
            AppEnv.DEV: 0,
            AppEnv.STAGING: 1,
            AppEnv.PROD: 2
        }

    @property
    def uri(self):
        scheme = 'redis://'
        password = f':{self.password}' if self.password else ''
        return f"{scheme}{password}@{self.host}:{self.port}/{self.db_number}"

    @property
    def db_number(self):
        return self.db_number_env[self.app_env]
