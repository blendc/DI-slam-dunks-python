from typing import Optional, List
from dataclasses import asdict
from ...domain.ports.user_repository import UserRepository
from ...domain.entities.user import User


class CachedUserRepository(UserRepository):
    def __init__(self, repository: UserRepository, cache):
        self.repository = repository
        self.cache = cache
    
    async def get_by_email(self, email: str) -> Optional[User]:
        cache_key = f"user:email:{email}"
        cached_data = self.cache.get(cache_key)
        
        if cached_data:
            return User(**cached_data)
        
        user = await self.repository.get_by_email(email)
        
        if user:
            self.cache.set(cache_key, asdict(user), ttl=300)
        
        return user
    
    async def get_by_id(self, user_id: int) -> Optional[User]:
        cache_key = f"user:id:{user_id}"
        cached_data = self.cache.get(cache_key)
        
        if cached_data:
            return User(**cached_data)
        
        user = await self.repository.get_by_id(user_id)
        
        if user:
            self.cache.set(cache_key, asdict(user), ttl=300)
        
        return user
    
    async def create(self, user: User) -> User:
        created_user = await self.repository.create(user)
        return created_user
    
    async def update(self, user: User) -> User:
        updated_user = await self.repository.update(user)
        
        self.cache.delete(f"user:id:{user.id}")
        if user.email:
            self.cache.delete(f"user:email:{user.email}")
        
        return updated_user
    
    async def list(self, skip: int = 0, limit: int = 100) -> List[User]:
        return await self.repository.list(skip, limit)
    
    async def delete(self, user_id: int) -> bool:
        user = await self.repository.get_by_id(user_id)
        
        if user:
            self.cache.delete(f"user:id:{user_id}")
            if user.email:
                self.cache.delete(f"user:email:{user.email}")
        
        return await self.repository.delete(user_id)
