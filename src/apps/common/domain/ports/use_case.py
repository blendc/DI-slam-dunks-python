from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')
R = TypeVar('R')

class UseCasePort(Generic[T, R], ABC):
    @abstractmethod
    def execute(self, data: T) -> R:
        pass 