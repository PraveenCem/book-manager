from bson import ObjectId
from app.core.database import db
from app.models.book import BookCreate,BookUpdate
from datetime import datetime
from typing import List


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
        result = await db.db['books'].delete_one({"_id":ObjectId(book_id)})
        return result.deleted_count > 0

    @staticmethod
    async def get_book(book_id:str):
        book = await db.db['books'].find_one({
            "_id": ObjectId(book_id)
        })

        if book:
            book["_id"] = str(book["_id"])

        return book

    @staticmethod
    async def update(book_id:str,book_data:dict):
        result = await db.db['books'].update_one(
            {"_id": ObjectId(book_id)},
            {"$set": book_data}
        )

        if result.matched_count == 0:
            return None

        updated_book = await db.db['books'].find_one(
            {"_id": ObjectId(book_id)}
        )

        updated_book["_id"] = str(updated_book["_id"])

        return updated_book

    @staticmethod
    async def filter_books(author:str,min_year:int=None,max_year:int=None,genres:List[str]=None,sort_by:str=None,sort_order:str="asc"):
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
            query["genres"] = {
                "$in":genres
            }

        if sort_by:
            sort_direction = 1 if sort_order == "asc" else -1

        cursor = db.db["books"].find(query).sort(sort_by,sort_direction)

        async for document in cursor:
            document["_id"] = str(document["_id"])
            books.append(document)

        return books