from dataclasses import dataclass
from typing import Optional
from starlette.requests import Request as StarletteRequest


def get_client_host(request: StarletteRequest) -> str:
    """Return the client host from a Starlette request."""
    return request.client.host if request.client else "unknown"

@dataclass
class Request:
    user_id: Optional[int] = None 