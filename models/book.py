from datetime import time
from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str
    created_at: time

class BookResponse:
    id: int
    title: str
    author: str
    created_at: time