import os
from enum import Enum, unique


def get_postgres_uri(dbname, user, password, host, port=5432):
    return f'postgresql://{user}:{password}@{host}:{port}/{dbname}'


def get_db_url() -> str:
    return get_postgres_uri(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
    )


@unique
class AppEnv(Enum):
    DEV = 'DEV'
    STAGING = 'STAGING'
    PROD = 'PROD'
