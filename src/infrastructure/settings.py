import os

from infrastructure.config import AppEnv

APP_ENV = os.getenv('APP_ENV', AppEnv.DEV.value)
SENTRY_DSN = os.getenv('SENTRY_DSN')
DEBUG = APP_ENV == AppEnv.DEV.value
VERSION = os.getenv('VERSION')
SECRET_KEY = os.getenv('SECRET_KEY')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = 720
PAGE_SIZE = 50
DEFAULT_CHUNK_SIZE = 3000
API_KEY = os.getenv('API_KEY')
API_KEY_HEADER = 'Authorization'
