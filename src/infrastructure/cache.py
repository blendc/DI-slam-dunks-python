import json
from typing import Optional, Any
import redis
import os


class RedisCache:
    def __init__(self):
        redis_host = os.getenv('REDIS_HOST', 'localhost')
        redis_port = int(os.getenv('REDIS_PORT', 6379))
        redis_password = os.getenv('REDIS_PASSWORD', None)
        
        self.client = redis.Redis(
            host=redis_host,
            port=redis_port,
            password=redis_password,
            db=3,
            decode_responses=True
        )
    
    def get(self, key: str) -> Optional[Any]:
        value = self.client.get(key)
        return json.loads(value) if value else None
    
    def set(self, key: str, value: Any, ttl: int = 300):
        self.client.setex(key, ttl, json.dumps(value, default=str))
    
    def delete(self, key: str):
        self.client.delete(key)
    
    def clear_pattern(self, pattern: str):
        for key in self.client.scan_iter(match=pattern):
            self.client.delete(key)
    
    def exists(self, key: str) -> bool:
        return bool(self.client.exists(key))
