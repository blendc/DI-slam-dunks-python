from dependency_injector import containers, providers
from ..adapters.repositories.user import SQLAlchemyUserRepository
from ..adapters.repositories.cached_user import CachedUserRepository
from ..domain.use_cases.get_current_user import GetCurrentUserUseCase
from src.infrastructure.db import Database


class AuthPackage(containers.DeclarativeContainer):
    database = providers.Dependency()
    cache = providers.Dependency()
    
    base_user_repository = providers.Factory(
        SQLAlchemyUserRepository,
        session=database.provided.session
    )
    
    user_repository = providers.Factory(
        CachedUserRepository,
        repository=base_user_repository,
        cache=cache
    )

    get_current_user_use_case = providers.Factory(
        GetCurrentUserUseCase,
        user_repository=user_repository
    )
