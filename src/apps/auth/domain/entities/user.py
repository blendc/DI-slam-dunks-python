from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class User:
    email: str
    password_hash: str
    is_active: bool = True
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def deactivate(self) -> None:
        self.is_active = False

    def activate(self) -> None:
        self.is_active = True
