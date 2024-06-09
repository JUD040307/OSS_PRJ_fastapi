from pydantic import BaseModel
from datetime import datetime

class GuestbookEntry(BaseModel):
    id: int
    author: str
    content: str
    timestamp: datetime
