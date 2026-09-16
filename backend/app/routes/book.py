from fastapi import APIRouter,Query
from app.models.book import BookCreate,BookUpdate,Review
from app.models.book_repo import BookRepository
from typing import List


router = APIRouter()

@router.post("/books")
async def create_book(book:BookCreate):
    return await BookRepository.create(book.model_dump())

@router.get("/books")
async def get_books(author:str=Query(None,min_length=3),
                    min_year:int=None,
                    max_year:int=None,
                    genres:str=None,
                    sort_by:str=None,
                    sort_order:str="asc",
                    page:int=1,
                    page_size:int=10,
                    exclude_year:int=None,
                    exclude_genres:str = None,
                    search:str=None):
    genre_list = genres.split(",") if genres else None
    exclude_genres_list = exclude_genres.split(",") if exclude_genres else None
    skip = (page-1) * page_size
    result =  await BookRepository.filter_books(
        author,
        min_year,
        max_year,
        genre_list,
        sort_by,
        sort_order,
        page_size,
        skip,
        exclude_year,
        exclude_genres_list,
        search)

    return{
        "books": result['books'],
        "page": page,
        "page_size": page_size,
        "total": result["total"],
        "total_pages": result["total_pages"]
    }

@router.get("/books/stats/genres")
async def genre_stats():
    return await BookRepository.genre_stats()

@router.get("/books/stats")
async def book_stats():
    return await BookRepository.book_stats()

@router.post("/books/{book_id}/reviews")
async def add_review(book_id:str, review:Review):
    return await BookRepository.add_review(
        book_id,
        review.model_dump()
    )

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


