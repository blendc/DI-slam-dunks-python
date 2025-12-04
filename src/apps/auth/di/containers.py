from dependency_injector import containers, providers
from ..adapters.repositories.user import SQLAlchemyUserRepository
from ..domain.use_cases.get_current_user import GetCurrentUserUseCase
from src.infrastructure.db import Database


class AuthPackage(containers.DeclarativeContainer):
    database = providers.Dependency()
    
    user_repository = providers.Factory(
        SQLAlchemyUserRepository,
        session=database.provided.session
    )

    get_current_user_use_case = providers.Factory(
        GetCurrentUserUseCase,
        user_repository=user_repository
    )
