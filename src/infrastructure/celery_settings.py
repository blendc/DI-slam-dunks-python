import os

from .config import AppEnv
from .redis import RedisConfig

app_env = os.getenv('APP_ENV', 'DEV')
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = os.getenv('REDIS_PORT', 6379)
redis_password = os.getenv('REDIS_PASSWORD', None)
redis_config = RedisConfig(redis_host, redis_port, AppEnv(app_env), redis_password)

broker_url = redis_config.uri
result_backend = redis_config.uri
accept_content = ['application/json']
enable_utc = True
broker_pool_limit = None

task_acks_late = True
broker_heartbeat = 0
worker_prefetch_multiplier = 1

worker_send_task_events = True
task_track_started = True


