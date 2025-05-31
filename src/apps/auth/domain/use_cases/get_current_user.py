from typing import Optional
from ...domain.entities.user import User
from ...domain.ports.user_repository import UserRepository
from apps.common.domain.ports.use_case import UseCasePort


class GetCurrentUserUseCase(UseCasePort[int, Optional[User]]):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: int) -> Optional[User]:
        return self.user_repository.get_by_id(user_id) 