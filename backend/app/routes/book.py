from fastapi import APIRouter,Query
from app.models.book import BookCreate,BookUpdate
from app.models.book_repo import BookRepository
from typing import List


router = APIRouter()

@router.post("/books")
async def create_book(book:BookCreate):
    return await BookRepository.create(book.model_dump())

@router.get("/books")
async def get_books(author:str=Query(None,min_length=3),min_year:int=None,max_year:int=None,genres:str=None,sort_by:str=None,sort_order:str="asc"):
    genre_list = genres.split(",") if genres else None

    return await BookRepository.filter_books(author,min_year,max_year,genre_list,sort_by,sort_order)

@router.get("/books/{book_id}")
async def get_book(book_id:str):
    return await BookRepository.get_book(book_id)

@router.patch("/books/{book_id}")
async def update_book(book_id:str, book:BookUpdate):
    return await BookRepository.update(
        book_id,
        book.model_dump(exclude_none=True)
    )

@router.delete("/books/{book_id}")
async def delete_book(book_id:str):
    return await BookRepository.delete(book_id)