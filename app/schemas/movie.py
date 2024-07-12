from typing import List
from pydantic import BaseModel

class Movie(BaseModel):
    id: int
    title: str
    description: str
    categories: List
    age = int
    raiting: float

