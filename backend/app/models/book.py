from pydantic import BaseModel,Field
from typing import Optional, List

class Review(BaseModel):
    user: str
    rating: int = Field(...,ge=1,le=5)
    comment: str

class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    genres: List[str] = []

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None
    genres: Optional[List[str]] = None

class BookInDB(BookCreate):
    id: str = Field(alias="_id")
    reviews: List[Review] = []

    class Config:
        populate_by_name = True