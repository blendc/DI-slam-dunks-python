from dependency_injector import containers, providers
from sqlalchemy.engine import make_url
from src.apps.auth.di.containers import AuthPackage
from src.infrastructure.celery import CeleryApp
from src.infrastructure.config import get_postgres_uri
from src.infrastructure.db import Database
from src.infrastructure.cache import RedisCache


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    config.app_env.from_env('APP_ENV')
    config.database.host.from_env('DB_HOST')
    config.database.password.from_env('DB_PASSWORD')
    config.database.user.from_env('DB_USER')
    config.database.name.from_env('DB_NAME')
    db_url = make_url(
        name_or_url=get_postgres_uri(
            dbname=config.database.name(),
            user=config.database.user(),
            password=config.database.password(),
            host=config.database.host(),
        )
    )
    database = providers.Singleton(Database, db_url)
    celery_app = providers.Singleton(CeleryApp)
    cache = providers.Singleton(RedisCache)

    auth_package = providers.Container(
        AuthPackage,
        database=database,
        cache=cache
    )


container = AppContainer()
