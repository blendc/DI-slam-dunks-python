from fastapi import FastAPI
from src.infrastructure import settings

app = FastAPI(
    debug=settings.DEBUG,
    title='API Tezja Cakit',
    version=settings.VERSION,
    docs_url='/'
)


