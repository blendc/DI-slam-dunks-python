from contextlib import asynccontextmanager
from typing import AsyncGenerator
from sqlalchemy.orm import Session
from ..domain.ports.user_repository import UserRepository
from .repositories.user import SQLAlchemyUserRepository


class UnitOfWork:
    def __init__(self, session: Session):
        self.session = session
        self.user_repository: UserRepository = SQLAlchemyUserRepository(session)

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()


@asynccontextmanager
async def get_unit_of_work(session: Session) -> AsyncGenerator[UnitOfWork, None]:
    uow = UnitOfWork(session)
    try:
        yield uow
        await uow.commit()
    except Exception:
        await uow.rollback()
        raise
