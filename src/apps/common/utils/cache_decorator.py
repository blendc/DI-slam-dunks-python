from functools import wraps
from typing import Callable, Any
import hashlib
import json


def cache_key(*args, **kwargs) -> str:
    key_data = json.dumps({"args": args, "kwargs": kwargs}, sort_keys=True, default=str)
    return hashlib.md5(key_data.encode()).hexdigest()


def cached(prefix: str, ttl: int = 300):
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if not hasattr(self, 'cache'):
                return func(self, *args, **kwargs)
            
            key = f"{prefix}:{cache_key(*args, **kwargs)}"
            
            cached_result = self.cache.get(key)
            if cached_result is not None:
                return cached_result
            
            result = func(self, *args, **kwargs)
            
            if result is not None:
                self.cache.set(key, result, ttl)
            
            return result
        return wrapper
    return decorator
