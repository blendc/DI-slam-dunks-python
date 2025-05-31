from dataclasses import dataclass
from typing import Optional


@dataclass
class Request:
    user_id: Optional[int] = None 