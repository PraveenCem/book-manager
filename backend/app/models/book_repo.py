from bson import ObjectId
from app.core.database import db
from app.models.book import BookCreate,BookUpdate
from datetime import datetime
from typing import List
from fastapi import HTTPException

class BookRepository:
    @staticmethod
    async def get_all():
        books = []
        cursor = db.db['books'].find({})
        async for document in cursor:
            document["_id"] = str(document["_id"])
            books.append(document)
        return books
    
    @staticmethod
    async def create(book_data:dict):
        result = await db.db['books'].insert_one(book_data)
        new_book = await db.db['books'].find_one({"_id":result.inserted_id})
        new_book["_id"] = str(new_book["_id"])
        return new_book

    @staticmethod 
    async def delete(book_id:str):
        try:
            object_id = ObjectId(book_id)
        except Exception:
            raise HTTPException(
                status_code=400,
                detail="Invalid book id"
            )
        
        result = await db.db['books'].delete_one({"_id":ObjectId(book_id)})
        if result.deleted_count == 0:
            raise HTTPException(
                status_code=404,
                detail="Book not found"
            )

        return{
            "message": "Book deleted succesfully."
        }

    @staticmethod
    async def get_book(book_id:str):
        try:
            object_id = ObjectId(book_id)
        except Exception:
            raise HTTPException(
                status_code=400,
                detail="Invalid book id"
            )
        
        book = await db.db['books'].find_one({
            "_id": object_id
        })

        if book is None:
            raise HTTPException(
                status_code=404,
                detail="Book not found"
            )

        book["_id"] = str(book["_id"])

        return book

    @staticmethod
    async def update(book_id:str,book_data:dict):

        try:
            object_id = ObjectId(book_id)
        except Exception:
            raise HTTPException(
                status_code=400,
                detail="Invalid book id"
            )


        result = await db.db['books'].update_one(
            {"_id": ObjectId(book_id)},
            {"$set": book_data}
        )

        if result.matched_count == 0:
            raise HTTPException(
                status_code=404,
                detail="book not found"
            )

        updated_book = await db.db['books'].find_one(
            {"_id": ObjectId(book_id)}
        )

        updated_book["_id"] = str(updated_book["_id"])

        return updated_book

    @staticmethod
    async def filter_books(author:str,
                           min_year:int=None,
                           max_year:int=None,
                           genres:List[str]=None,
                           sort_by:str=None,
                           sort_order:str="asc",
                           limit:int=None,
                           skip:int=None,
                           exclude_year:int=None,
                           exclude_genres:List[str]=None,
                           search:str=None):
        books = []

        query = {}

        if author:
            query['author'] = {
                "$regex": author,
                "$options": "i"
            }

        if min_year:
            query['year'] = {
                "$gte": min_year,
                "$lte":datetime.now().year
            }

        if max_year:
            query.setdefault("year",{})["$lte"] = max_year

        if genres:
            query.setdefault("genres",{})["$in"] = genres

        if exclude_genres:
            query.setdefault("genres",{})["$nin"] = exclude_genres
        
        if exclude_year:
            query.setdefault("year",{})["$ne"] =  exclude_year

        if search:
                query["$or"]= [{
                    "title":{
                        "$regex": search,
                        "$options": "i"
                    }
                },
                {
                    "author":{
                        "$regex": search,
                        "$options":"i"
                    }
                },
                {
                    "genres":{
                        "$regex": search,
                        "$options": "i"
                    }
                }
                ]
            
        total = await db.db["books"].count_documents(query)
        cursor = db.db["books"].find(query)

        if sort_by:
            sort_direction = 1 if sort_order == "asc" else -1
            cursor = cursor.sort(sort_by,sort_direction)

        if limit:
            cursor = cursor.limit(limit)

        if skip:
            cursor = cursor.skip(skip)


        total_pages = (total+limit-1) // limit

        async for document in cursor:
            document["_id"] = str(document["_id"])
            books.append(document)

        return {
            "books": books,
            "total": total,
            "total_pages": total_pages
        }

    @staticmethod
    async def genre_stats():
        pipeline = [
            {"$unwind":"$genres"},
            {
                "$group":{
                    "_id": "$genres",
                    "count": {"$sum":1}
                }
            }
        ]

        result = []

        async for document in db.db["books"].aggregate(pipeline):
            result.append({
                "genre": document["_id"],
                "count": document["count"]
            })

        return result


    @staticmethod
    async def book_stats():
        pipeline = [
            {
                "$group": {
                    "_id": None,
                    "total_books": {"$sum": 1},
                    "average_year": {"$avg": "$year"},
                    "oldest_year": {"$min": "$year"},
                    "newest_year":{"$max":"$year"}
                }
            }
        ]

        result = []

        async for document in db.db["books"].aggregate(pipeline):
            result.append({
                "total_books": document["total_books"],
                "average_year":document["average_year"],
                "oldest_year":document["oldest_year"],
                "newest_year":document["newest_year"]
            })

        return result

    @staticmethod
    async def add_review(book_id:str,review_data:dict):
        result = await db.db["books"].update_one(
            {"_id": ObjectId(book_id)},
            {"$push":{"reviews":review_data}}
        )

        if result.matched_count == 0:
            return None

        updated_book = await db.db["books"].find_one(
            {"_id": ObjectId(book_id)}
        )

        updated_book["_id"] = str(updated_book["_id"])

        return updated_book

    @staticmethod
    async def get_reviews(book_id:str):

        try:
            object_id = ObjectId(book_id)
        except Exception:
            raise HTTPException(
                status_code=400,
                detail="Invalid book id"
            )

        book = await db.db["books"].find_one(
            {"_id":object_id},
            {"reviews":1}
        )

        if book is None:
            raise HTTPException(
                status_code=404,
                detail="book not found"
            )

        return book.get("reviews",[])

    @staticmethod
    async def update_review(
        book_id: str,
        user: str,
        review_data: dict
    ):

        try:
            object_id = ObjectId(book_id)
        except Exception:
            raise HTTPException(
                status_code=400,
                detail="invalid book id"
            )

        book = await db.db["books"].find_one(
                    {"_id": ObjectId(book_id)},
                    {"reviews": 1}
                )
        
        if book is None:
            raise HTTPException(
                status_code=404,
                detail="Book not found"
            )

        result = await db.db["books"].update_one(
            {
                "_id":object_id,
                "reviews.user": user
            },
            {
                "$set":{
                    "reviews.$":review_data
                }
            }
        )

        if result.matched_count == 0:
            raise HTTPException(
                status_code=404,
                detail="review not found"
            )

        

        return book.get("reviews",[])


    @staticmethod
    async def delete_review(book_id:str,user:str):

        try:
            object_id = ObjectId(book_id)
        except Exception:
            raise HTTPException(
                status_code=400,
                detail="invalid book id"
            )

        book = await db.db["books"].find_one(
            {"_id": object_id},
            {"reviews": 1}
        )
        
        if book is None:
            raise HTTPException(
                status_code=404,
                detail="Book not found"
            )

        result = await db.db["books"].update_one(
            {"_id":object_id},
            {
                "$pull":{
                    "reviews":{
                        "user":user
                    }
                }
            }
        )

        if result.modified_count == 0:
            raise HTTPException(
                status_code=404,
                detail="Review not found"
            )

  
        return book.get("reviews",[])