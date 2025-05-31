from typing import Optional, List
from sqlalchemy.orm import Session
from ...domain.ports.user_repository import UserRepository
from ...domain.entities.user import User
from ...infrastructure.orm import UserModel


class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    async def get_by_email(self, email: str) -> Optional[User]:
        user_model = self.session.query(UserModel).filter_by(email=email).first()
        if user_model:
            return User(
                id=user_model.id,
                email=user_model.email,
                password_hash=user_model.password_hash,
                is_active=user_model.is_active,
                created_at=user_model.created_at,
                updated_at=user_model.updated_at
            )
        return None

    async def get_by_id(self, user_id: int) -> Optional[User]:
        user_model = self.session.query(UserModel).filter_by(id=user_id).first()
        if user_model:
            return User(
                id=user_model.id,
                email=user_model.email,
                password_hash=user_model.password_hash,
                is_active=user_model.is_active,
                created_at=user_model.created_at,
                updated_at=user_model.updated_at
            )
        return None

    async def create(self, user: User) -> User:
        user_model = UserModel(
            email=user.email,
            password_hash=user.password_hash,
            is_active=user.is_active
        )
        self.session.add(user_model)
        self.session.commit()
        self.session.refresh(user_model)
        
        return User(
            id=user_model.id,
            email=user_model.email,
            password_hash=user_model.password_hash,
            is_active=user_model.is_active,
            created_at=user_model.created_at,
            updated_at=user_model.updated_at
        )

    async def update(self, user: User) -> User:
        user_model = self.session.query(UserModel).filter_by(id=user.id).first()
        if not user_model:
            raise ValueError(f"User with id {user.id} not found")

        user_model.email = user.email
        user_model.password_hash = user.password_hash
        user_model.is_active = user.is_active

        self.session.commit()
        self.session.refresh(user_model)

        return User(
            id=user_model.id,
            email=user_model.email,
            password_hash=user_model.password_hash,
            is_active=user_model.is_active,
            created_at=user_model.created_at,
            updated_at=user_model.updated_at
        )

    async def list(self, skip: int = 0, limit: int = 100) -> List[User]:
        user_models = self.session.query(UserModel).offset(skip).limit(limit).all()
        return [
            User(
                id=model.id,
                email=model.email,
                password_hash=model.password_hash,
                is_active=model.is_active,
                created_at=model.created_at,
                updated_at=model.updated_at
            )
            for model in user_models
        ]

    async def delete(self, user_id: int) -> bool:
        user_model = self.session.query(UserModel).filter_by(id=user_id).first()
        if not user_model:
            return False

        self.session.delete(user_model)
        self.session.commit()
        return True
